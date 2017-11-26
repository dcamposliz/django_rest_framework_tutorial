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

First thing to do for our Web API is providing a way of serializing and deserializing data into representations such as `json`. We can do this by declaring serializers that work very similarly to Django forms.

### [2. Requests and Responses](http://www.django-rest-framework.org/tutorial/2-requests-and-responses/)

REST framework introduces a `Request` object that extends the regular `HttpRequest`, and provides more flexible request parsing. The core functionality of the `Request` object is the `request.data` attribute, which is similar to `request.post`, but more useful for working with Web APIs. REST framework also introduces `Response` objects, which are a type of `TemplateResponse`.

### [3. Class-based Views](http://www.django-rest-framework.org/tutorial/3-class-based-views/)

We can write our API views using class-based views, rather than function based views. This is a powerful pattern that allows us to re-use code, and keep code DRY.

### [4. Authentication and Permissions](http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)

REST framework allows us to use Django's powerful authentication and authorization features for CRUD.

### [5. Relationships and Hyperlinked APIs](http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/)

Relationships within an API may be represented in many ways:

* using primary keys
* using hyperlinking between entities
* using a unique identifying string slug field on the related entity
* using the default string representation of the related entity
* nesting the related entity inside the parent representation
* others

We'd like to use hyperlinking between entitites, because this helps us improve the cohesion and discoverability of our API.

### [6. ViewSets and Routers](http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)

REST framework includes an abstraction for dealing with `ViewSets`, that allows developers to focus on modeling the state and interactions of the API, and leave the URL construction to be handled automatically, based on conventions.

`ViewSets` are similar to `View` classes, except, they provide operations such as `read`, or `update`, and not method handlers such as `get` or `put`.

A `ViewSet` class is only bound to a set of method handlers at the last moment, when it is instantiated into a set of views, typically using a `Router` class, which handles the complexities of defining the URL conf for you.

### [7. Schemas and Client Libraries](http://www.django-rest-framework.org/tutorial/7-schemas-and-client-libraries/)

A schema is a machine-readable document that describes the available API endpoints, their URLs, and what operations they support. Schemas can be useful for auto-generated documentation, as well as to drive dynamic client libraries that can interact with our API.