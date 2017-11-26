# Tutorial: Django REST Framework

Original docs:

* [1. Serialization](http://www.django-rest-framework.org/tutorial/1-serialization/)
* [2. Requests and Responses](http://www.django-rest-framework.org/tutorial/2-requests-and-responses/)
* [3. Class-based Views](http://www.django-rest-framework.org/tutorial/3-class-based-views/)
* [4. Authentication and Permissions](http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)
* [5. Relationships and Hyperlinked APIs](http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/)
* [6. ViewSets and Routers](http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)
* [7. Schemas and Client Libraries](http://www.django-rest-framework.org/tutorial/7-schemas-and-client-libraries/)

# Summary

### [1. Serialization](http://www.django-rest-framework.org/tutorial/1-serialization/)

...

### [2. Requests and Responses](http://www.django-rest-framework.org/tutorial/2-requests-and-responses/)

...

### [3. Class-based Views](http://www.django-rest-framework.org/tutorial/3-class-based-views/)

...

### [4. Authentication and Permissions](http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)

...

### [5. Relationships and Hyperlinked APIs](http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/)

...

### [6. ViewSets and Routers](http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)

REST framework includes an abstraction for dealing with `ViewSets`, that allows developers to focus on modeling the state and interactions of the API, and leave the URL construction to be handled automatically, based on conventions.

`ViewSets` are similar to `View` classes, except, they provide operations such as `read`, or `update`, and not method handlers such as `get` or `put`.

A `ViewSet` class is only bound to a set of method handlers at the last moment, when it is instantiated into a set of views, typically using a `Router` class, which handles the complexities of defining the URL conf for you.

### [7. Schemas and Client Libraries](http://www.django-rest-framework.org/tutorial/7-schemas-and-client-libraries/)

...