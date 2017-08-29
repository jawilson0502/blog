Deploying GRR has been a project I've been working on for the past month. One
of the biggest challenges I had was finding a way to deploy the services on
different servers so that it was easily scaled in the future. I decided that
the best way to do so was to create a server for the datastore, a server for
the front end HTTP service and a server for the worker services and admin
interface. I have created a walkthrough to do just that below.

## Assumptions made

While there are multiple ways to deploy a GRR server, below are the assumptions
made in order to deploy in the same manner I have.

* GRR Servers will be running Ubuntu 16.04 LTS with all updates already
installed.
* There will be 3 servers in the configuration as outlined above. They will be
called Master Dataserver, HTTP Server, and Main Server.
* Bleeding edge GRR is desired and will be installedvia pip.
* The virtual environment will be called GRR_NEW

## Setting up servers

This walkthrough assumes you've installed GRR from [GRR's installing from
pip](https://github.com/google/grr-doc/blob/master/installfrompip.adoc) page.
It is recommending you use the "tracking head" section.

## Configuring GRR on the Main Server

1. Set up a MTA of your choice
2. Run `grr_config_updater initialize`

    * Step 1: Key Generation: - this step autocompletes and needs no user input
    * Step 2: Setting Basic Configuration Parameters:

        * GRR Datastore: Choose `1` for a SQLite Datastore. That is the
        datastore all these tutorials assume you have.
        * GRR URLs: Enter hostname: `<main server ip>`
        * Server URL: Frontend URL `http://<http server ip>:8080/`
        * AdminUI URL: leave as default, press enter
        * GRR Emails: Email Domain: `<your email domain>`
        * GRR Emails: Alert Email Address: `<your alerts email>`
        * GRR Emails: Emergency Email Access Email Address: `<your emergency
        email>`
    * Step 3: Adding Admin User: `<password>`
    * Step 4: Installing template package: `n`
    * Step 5: - Completes on its own
    * _Optional_ - Edit `grr/install_data/etc/server.local.yaml` and move
    `Client.executable_signing_public_key` to a new file and change
    permissions based on your executable signing structure policy
    * _Optional_ - Set up the Approval Process
        * Users listed in the approval process will be added later. However
        this configuration must be pushed out to all servers, so it should be
        set up now.
        * Link to a post on how to manage ACLs coming soon

## Initial Configuration on HTTP Server

1. Replace `grr/install_data/etc/server.local.yaml` and
`grr/install_data/etc/grr-server.yaml` with the files from main server

## Configuration on Master Dataserver

1. Replace `grr/install_data/etc/server.local.yaml` and
`grr/install_data/etc/grr-server.yaml` with the files from main server.
2. Edit `grr/install_data/etc/server.local.yaml` and add the following:

```
Datastore.location: <full path to datastore>
Dataserver.server_list:
    - http://<dataserver ip>:7000
Dataserver.client_credentials:
    - <client_username>:<client_password>:rw
Dataserver.server_username: <server_username>
Dataserver.server_password: <server_password>
```

  Terms:
  * `server_list` is a list of all database servers with the master listed first
  * `client_credentials` are used for the http server and main server to
  communicate with the database.
  * `server_username` and `server_password` are used for any slave
  dataservers to talk to the master dataserver.

3. Start the dataserver service by running `grr_server --component
dataserver_master`
  * It should start with no errors and not show any information. If you would
    like to see more information add in `--verbose`

## Finish the configuration on the Main Server

1. Edit `install_data/etc/server.local.yaml`
    * Dataserver Configuration:                            

        ```
        Dataserver.server_list:
            - http://<dataserver ip>:7000
        Datastore.implementation: HTTPDataStore
        HTTPDataStore.username: <client_username>
        HTTPDataStore.password: <client_password>;
        ```

    * Email Configuration:

        ```
        Worker.smtp_server: <smtp server>
        Worker.smtp_port: <smtp port>
        Worker.smtp_starttlis: True
        Worker.smtp_user: <username>
        Worker.smtp_password: <password>>
        Email.approval_cc_address: <monitoring email>
        ```

        **Note** - `monitoring email` should only be the account name, the
         @domain is appended on later.
2. Add users who should be able to access the admin interface.
    * **Note** Users cannot change their password in the admin ui, they must
    change it in the command line.
    * [Managing Users Post]({{ url_for('post', blog_id=16) }})
3. Run `grr_config_updater repack_clients`
    * **Note** -If you decided to implement #3 in "Configuring GRR on the Main
    Server" add `--secondary_configs <signing key file>` after
    `grr_config_updater`

4. Start services with `grr_server --component worker` and `grr_server
--component ui`

## Finish the configuration on HTTP Server

1. Edit `install_data/etc/server.local.yaml`
    * Dataserver Configuration:                            

        ```
        Dataserver.server_list:
            - http://<dataserver ip>:7000
        Datastore.implementation: HTTPDataStore
        HTTPDatastore.username: <client_username>
        HTTPDatastore.password: <client_password>
        ```

2. Start services with `grr_server --component http_server`

## Almost there!
At this point you should be able to visit your admin ui and download the
installer binaries. Once that is installed on your client, it should be able to
communicate back to the HTTP server and everything should be stored within the
dataserver.
