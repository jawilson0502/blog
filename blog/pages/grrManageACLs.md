GRR provides a system for access control to the clients with a GRR agent
installed, which inlcudes an approval process. Below are the necessary steps to
set up this up based on the initial configuration in [GRR Server Setup]({{
url_for('post', blog_id=15) }}) **Note** - These
changes must be made on all GRR servers within your environment.

## Turn on ACLs
* Edit `grr/install_data/etc/grr-server.yaml`
* Find the `AdminUI Context:` section and add the following lines within that
section:

    ```
    Datastore.security_manager: FullAccessControlManager>
    API.DefaultRouter: ApiCallRouterWithApprovalChecksWithRobotAccess
    ```

## Create the ACLs
* Edit `grr/install_data/etc/approvers.yaml`
* Insert the following code:

    ```
    label: <machine label>
    requester_must_be_authorized: True
    num_approvers_required: 1
    users:
        - <username>
        - >username>
    ```
* Explanation of terms:
    * `label`: The label used for the machines
    * `requester_must_be_authorized`: If this is set to `True`, then only users
    listed in the users section may request access. This line is optional, if
    left out then any user can request access.
    * `num_approvers_required`: This specifies how many approvals must be given
    before the request can access a client.
    * `users`: This is a list of approvers for this label. If
    `request_must_be_authorized` is set to `True`it is also the list of users
    that are allowed to reqeust access to a machine.
* Restart all services if they were running

## Side notes
Ensure you have followed the [Manage Users]({{ url_for('post', blog_id=16) }})
walkthrough to create all the users you wish to have in your ACLs. Another
pitfall to be mindful of is that GRR will email the users involved in the
approval process, so ensure the username will provide a valid email address
when your email domain is appended to it.
