Managing users in GRR is critical to limit access. Below are a few key ways to
manage users.

## Add users
* Run `grr_config_updater add_user <username>`
* Enter the user's password when prompted.

## Change a user's password
* Run `grr_config_updater update_user <username> --password`
* Enter the new password when prompted

## Changing labels to user
* Adding labels: `grr_config_updater update_user <username> --add_labels
 <labels,comma,separated>`
* Deleting labels: `grr_config_updater update_user <username> --delete_ labels
<labels,comma,separated>`

## Listing users
* Run `grr_config_updater show_user <_optional_ username>`
* **Note** - If a user name is supplied, it will show only that user. If no
username is supplied, it shows all users.

## Deleting users
* Run `grr_config_updater delete_user <username>`
