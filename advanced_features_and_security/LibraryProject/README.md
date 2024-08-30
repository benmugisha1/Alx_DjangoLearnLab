Django Custom Permissions and Groups
Overview
This project demonstrates how to implement and manage custom permissions and groups to control access to various parts of the application. We have extended Django's default permissions system to include custom permissions for models, and enforced these permissions in the views.

Custom Permissions
We have defined the following custom permissions for the Document model:

can_view: Allows a user to view documents.
can_create: Allows a user to create new documents.
can_edit: Allows a user to edit existing documents.
can_delete: Allows a user to delete documents.
These permissions are defined in the Meta class of the Document model.

User Groups
We have set up the following user groups in the Django admin interface:

Viewers: Users in this group have the can_view permission.
Editors: Users in this group have the can_create and can_edit permissions.
Admins: Users in this group have all permissions, including can_delete.
Enforcing Permissions in Views
Permissions are enforced in views using the permission_required decorator. For example:

The view_document view checks for the can_view permission.
The create_document view checks for the can_create permission.
The edit_document view checks for the can_edit permission.
The delete_document view checks for the can_delete permission.
If a user tries to access a view without the required permission, they will be shown an error message or redirected to a different page.

Testing Permissions
To test the permissions:

Create users and assign them to different groups using the Django admin interface.
Log in as each user and attempt to access various views to verify that permissions are enforced correctly.
Ensure that users can only perform actions that they have permissions for.
Configuration Notes
Settings: The custom user model is specified in the settings.py file using the AUTH_USER_MODEL setting.
Migrations: After defining custom permissions, run python manage.py makemigrations and python manage.py migrate to apply the changes.
Future Enhancements
Implement more granular permissions as needed.
Expand the role-based access control system to include more complex scenarios.
