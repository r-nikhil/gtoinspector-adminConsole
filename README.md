## Admin Console

### Requirements

Discussed following are some of the requirements, ideas and techinques for making an admin dashboard for managing various End Users (hereon known as Users), and Admin Users (Us, hereon known as Admins)

1. Documentation: This would be a comprehensive guide on using the admin panel, and going forward, adding documentation on various other tools and basic troubleshooting
2. Creating New Users: This would be used to add new users to the database
3. Modifying Users: Enabling/Disabling, changing their name, generating new API Key, increasing validity
4. Mass updating user info: Changing a particular field for all the users in the system
5. Creating new services: If, going forward, if we need to add new services, this should not require changes to the codebase, this should be handled through this endpoint itself
6. Admin alerts: More on this would be updated in later iterations


The proposed infrastructure for this is as follows
1. MongoDB for storing user info: This makes sense because we would be dealing with multiple services, and maintaining an RDBMS at this rate would be hectic
2. Flask for creating server: Easy to set up, modify and maintain

Notes:
1. Use blueprints to make the module, instead of mapping everything to app itself. Blueprints allow for more modularity, and would help us changing/merging it with other parts of the server
2. Don't allow admin login directly. Admins should be enabled ONLY through root access, and not through any other source


### Some of the templates in the templates folder are copied as-is from the previous iteration. Feel free to use them or start afresh