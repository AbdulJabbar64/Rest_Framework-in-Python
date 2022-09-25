# Rest_Framework-in-Python

I have study some Video and i make those Points

# API

## How Web API Works ?
1. when client send HTTP requst to web API
2. API communcate with Web app database, it some needed
3. web API provader will return required data to API
4. API return data to Client

note: data may be in XML or JSON
## How USE Web API
1. register/signUP for API
2. API key/API token will provded to 
   - e.g API token = ksnfmkds8nksd887sand8
3. and client will commumacte with that api key
   - e.g: https://www.test?key=ksnfmkds8nksd887sand8
4. if API auth successed then API provde data to Client, if auth **not** successed it return API is not authunted

## Serializers and Deserializers
**Serializers** allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide **deserialization**, allowing parsed data to be converted back into complex types, after first validating the incoming data.

## Validation
When deserializing data, you always need to call **is_valid()** before attempting to access the validated data, or save an object instance. If any validation errors occur, the .errors property will contain a dictionary representing the resulting error messages.


#### There are three type of validation
1. Field Level Validation
2. Object Level Validation
3. Validators

## ModelSerializer
The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.

**The ModelSerializer class is the same as a regular Serializer class, except that:**
- It will automatically generate a set of fields for you, based on the model.
- It will automatically generate validators for the serializer, such as unique_together validators.
- It includes simple default implementations of **.create()** and **.update()**.

## Class Based Views
REST framework provides an APIView class, which subclasses Django's View class.

**APIView** classes are different from regular **View** classes in the following ways:

- Requests passed to the handler methods will be REST framework's **Request** instances, not Django's **HttpRequest** instances.
- Handler methods may return REST framework's **Response**, instead of Django's **HttpResponse**. The view will manage content negotiation and setting the correct renderer on the response.
- Any **APIException** exceptions will be caught and mediated into appropriate responses.
- Incoming requests will be authenticated and appropriate permission and/or throttle checks will be run before dispatching the request to the handler method.

## Function Based Views
REST framework also allows you to work with regular function based views. It provides a set of simple decorators that wrap your function based views to ensure they receive an instance of **Request** (rather than the usual Django **HttpRequest**) and allows them to return a **Response** (instead of a Django **HttpResponse**), and allow you to configure how the request is processed.


## GenericAPIView
This class extends REST framework's **APIView** class, adding commonly required behavior for standard list and detail views.

Each of the concrete generic views provided is built by combining GenericAPIView, with one or more mixin classes.

#### Attributes
- **queryset** - The queryset that should be used for returning objects from this view. Typically, you must either set this attribute, or override the **get_queryset()** method. If you are overriding a view method, it is important that you call **get_queryset()** instead of accessing this property directly, as **queryset** will get evaluated once, and those results will be cached for all subsequent requests.
- **serializer_class** - The serializer class that should be used for validating and deserializing input, and for serializing output. Typically, you must either set this attribute, or override the **get_serializer_class()** method.
- **lookup_field** - The model field that should be used to for performing object lookup of individual model instances. Defaults to **'pk'**. Note that when using hyperlinked APIs you'll need to ensure that both the API views and the serializer classes set the lookup fields if you need to use a custom value.
- **lookup_url_kwarg** - The URL keyword argument that should be used for object lookup. The URL conf should include a keyword argument corresponding to this value. If unset this defaults to using the same value as **lookup_field**.

## Concrete View Classes
The following classes are the concrete generic views. If you're using generic views this is normally the level you'll be working at unless you need heavily customized behavior.

The view classes can be imported from **rest_framework.generics**.

- **CreateAPIView**: Used for create-only endpoints. Provides a post method handler. 
- **ListAPIView**: Used for read-only endpoints to represent a collection of model instances. Provides a get method handler.
- **RetrieveAPIView**: Used for read-only endpoints to represent a single model instance. Provides a get method handler.
- **DestroyAPIView**: Used for delete-only endpoints for a single model instance. Provides a delete method handler.
- **UpdateAPIView**: Used for update-only endpoints for a single model instance.Provides put and patch method handlers.
- **ListCreateAPIView**: Used for read-write endpoints to represent a collection of model instances. Provides get and post method handlers.
- **RetrieveUpdateAPIView**: Used for read or update endpoints to represent a single model instance. Provides get, put and patch method handlers.
- **RetrieveDestroyAPIView**: Used for read or delete endpoints to represent a single model instance. Provides get and delete method handlers.
- **RetrieveUpdateDestroyAPIView**: Used for read-write-delete endpoints to represent a single model instance. Provides get, put, patch and delete method handlers.

## ViewSets
Django REST framework allows you to combine the logic for a set of related views in a single class, called a **ViewSet**. In other frameworks you may also find conceptually similar implementations named something like 'Resources' or 'Controllers'.

A **ViewSet** class is simply a type of class-based View, that does not provide any method handlers such as **.get()** or **.post()**, and instead provides actions such as **.list()** and **.create()**.

The method handlers for a **ViewSet** are only bound to the corresponding actions at the point of finalizing the view, using the **.as_view()** method.

#### ViewSet actions
During dispatch, the following attributes are available on the ViewSet.

- **basename** - the base to use for the URL names that are created.
- **action** - the name of the current action (e.g., **list**, **create**).
- **detail** - boolean indicating if the current action is configured for a list or detail view.
- **suffix** - the display suffix for the viewset type - mirrors the detail attribute.
- **name** - the display name for the viewset. This argument is mutually exclusive to **suffix**.
- **description** - the display description for the individual view of a viewset.

## ModelViewSet
The **ModelViewSet** class inherits from **GenericAPIView** and includes implementations for various actions, by mixing in the behavior of the various mixin classes.

The actions provided by the **ModelViewSet** class are **.list()**, **.retrieve()**, **.create()**, **.update()**, **.partial_update()**, and **.destroy()**.

## Authentication
Authentication is the mechanism of associating an incoming request with a set of identifying credentials, such as the user the request came from, or the token that it was signed with. The **permission** and **throttling** policies can then use those credentials to determine if the request should be permitted.

REST framework provides several authentication schemes out of the box, and also allows you to implement custom schemes.

Authentication always runs at the very start of the view, before the permission and throttling checks occur, and before any other code is allowed to proceed.

The **request.user** property will typically be set to an instance of the **contrib.auth** package's **User** class.

The **request.auth** property is used for any additional authentication information, for example, it may be used to represent an authentication token that the request was signed with.

## API Reference
- **BasicAuthentication**
- **SessionAuthentication**
- **RemoteUserAuthentication**
- **Custom authentication**
- **TokenAuthentication**

## BasicAuthentication
This authentication scheme uses HTTP Basic Authentication, signed against a user's username and password. Basic authentication is generally only appropriate for testing.

If successfully authenticated, **BasicAuthentication** provides the following credentials.

**request.user** will be a Django **User** instance.
**request.auth** will be **None**.
Unauthenticated responses that are denied permission will result in an **HTTP 401 Unauthorized** response with an appropriate WWW-Authenticate header. For example:

``WWW-Authenticate: Basic realm="api"``

## SessionAuthentication
This authentication scheme uses Django's default session backend for authentication. Session authentication is appropriate for AJAX clients that are running in the same session context as your website.

If successfully authenticated, **SessionAuthentication** provides the following credentials.

**request.user** will be a Django **User** instance.
**request.auth** will be **None**.
Unauthenticated responses that are denied permission will result in an **HTTP 403 Forbidden** response.

If you're using an AJAX-style API with **SessionAuthentication**, you'll need to make sure you include a valid **CSRF** token for any "unsafe" HTTP method calls, such as **PUT**, **PATCH**, **POST** or **DELETE** requests. See the [Django CSRF documentation](https://docs.djangoproject.com/en/4.1/ref/csrf/#ajax) for more details.

## TokenAuthentication
This authentication scheme uses a simple token-based HTTP Authentication scheme. Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.

To use the **TokenAuthentication** scheme you'll need to configure the authentication classes to include **TokenAuthentication**, and additionally include **rest_framework.authtoken** in your **INSTALLED_APPS** setting:

``INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]``

Make sure to **run manage.py migrate** after changing your settings.

The **rest_framework.authtoken** app provides Django database migrations.

For clients to authenticate, the token key should be included in the **Authorization** HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

``Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b``
## RemoteUserAuthentication
This authentication scheme allows you to delegate authentication to your web server, which sets the **REMOTE_USER** environment variable.

To use it, you must have **django.contrib.auth.backends.RemoteUserBackend** (or a subclass) in your **AUTHENTICATION_BACKENDS** setting. By default, RemoteUserBackend creates **User** objects for usernames that don't already exist. To change this and other behaviour, consult the [Django documentation](https://docs.djangoproject.com/en/4.1/howto/auth-remote-user/).

If successfully authenticated, **RemoteUserAuthentication** provides the following credentials:

**request.user** will be a Django **User** instance.
**request.auth** will be **None**.


## Permissions
Together with **authentication** and **throttling**, permissions determine whether a request should be granted or denied access.

Permission checks are always run at the very start of the view, before any other code is allowed to proceed. Permission checks will typically use the authentication information in the **request.user** and **request.auth** properties to determine if the incoming request should be permitted.

Permissions are used to grant or deny access for different classes of users to different parts of the API.

The simplest style of permission would be to allow access to any authenticated user, and deny access to any unauthenticated user. This corresponds to the **IsAuthenticated** class in REST framework.

A slightly less strict style of permission would be to allow full access to authenticated users, but allow read-only access to unauthenticated users. This corresponds to the **IsAuthenticatedOrReadOnly** class in REST framework.

### How permissions are determined
Before running the main body of the view each permission in the list is checked. If any permission check fails, an **exceptions.PermissionDenied** or **exceptions.NotAuthenticated** exception will be raised, and the main body of the view will not run.

When the permission checks fail, either a "403 Forbidden" or a "401 Unauthorized" response will be returned, according to the following rules:

- The request was successfully authenticated, but permission was denied. — <i><b> An HTTP 403 Forbidden response will be returned </b></i>.
- The request was not successfully authenticated, and the highest priority authentication class does not use **WWW-Authenticate** headers. — <i><b>An HTTP 403 Forbidden response will be returned </b></i>.
- The request was not successfully authenticated, and the highest priority authentication class does use **WWW-Authenticate** headers. — <i><b>An HTTP 401 Unauthorized response</b></i>, with an appropriate **WWW-Authenticate** header will be returned.

## Throttling
Throttling is similar to permissions, in that it determines if a request should be authorized. Throttles indicate a temporary state, and are used to control the rate of requests that clients can make to an API.

As with permissions, multiple throttles may be used. Your API might have a restrictive throttle for unauthenticated requests, and a less restrictive throttle for authenticated requests.

Another scenario where you might want to use multiple throttles would be if you need to impose different constraints on different parts of the API, due to some services being particularly resource-intensive.

Multiple throttles can also be used if you want to impose both burst throttling rates, and sustained throttling rates. For example, you might want to limit a user to a maximum of 60 requests per minute, and 1000 requests per day.


### AnonRateThrottle
The **AnonRateThrottle** will only ever throttle unauthenticated users. The IP address of the incoming request is used to generate a unique key to throttle against.

The allowed request rate is determined from one of the following (in order of preference).

- The **rate** property on the class, which may be provided by overriding **AnonRateThrottle** and setting the property.
- The **DEFAULT_THROTTLE_RATES['anon']** setting.

**AnonRateThrottle** is suitable if you want to restrict the rate of requests from unknown sources.

### UserRateThrottle
The **UserRateThrottle** will throttle users to a given rate of requests across the API. The user id is used to generate a unique key to throttle against. Unauthenticated requests will fall back to using the IP address of the incoming request to generate a unique key to throttle against.

The allowed request rate is determined from one of the following (in order of preference).

- The **rate** property on the class, which may be provided by overriding UserRateThrottle and setting the property.
- The **DEFAULT_THROTTLE_RATES['user']** setting.

An API may have multiple **UserRateThrottles** in place at the same time. To do so, override UserRateThrottle and set a unique "scope" for each class.

### ScopedRateThrottle
The **ScopedRateThrottle** class can be used to restrict access to specific parts of the API. This throttle will only be applied if the view that is being accessed includes a **.throttle_scope** property. The unique throttle key will then be formed by concatenating the "scope" of the request with the unique user id or IP address.

The allowed request rate is determined by the **DEFAULT_THROTTLE_RATES** setting using a key from the request "scope".

## Filtering
The simplest way to filter the queryset of any view that subclasses **GenericAPIView** is to override the **.get_queryset()** method.

Overriding this method allows you to customize the queryset returned by the view in a number of different ways.

## Pagination
The pagination API has been improved, making it both easier to use, and more powerful.

Note that as a result of this work a number of settings keys and generic view attributes are now moved to pending deprecation. Controlling pagination styles is now largely handled by overriding a pagination class and modifying its configuration attributes.

- The **PAGINATE_BY** settings key will continue to work but is now pending deprecation. The more obviously named **PAGE_SIZE** settings key should now be used instead.
- The **PAGINATE_BY_PARAM**, **MAX_PAGINATE_BY** settings keys will continue to work but are now pending deprecation, in favor of setting configuration attributes on the configured pagination class.
- The **paginate_by**, **page_query_param**, **paginate_by_param** and **max_paginate_by** generic view attributes will continue to work but are now pending deprecation, in favor of setting configuration attributes on the configured pagination class.
- The **pagination_serializer_class** view attribute and **DEFAULT_PAGINATION_SERIALIZER_CLASS** settings key are no longer valid. The pagination API does not use serializers to determine the output format, and you'll need to instead override the **get_paginated_response** method on a pagination class in order to specify how the output format is controlled.
