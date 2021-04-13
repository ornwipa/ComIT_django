# Tutorial: The Local Library Website

This tutorial extends the website to add a session-based visit-counter to the home page.

## Session framework

All communication between web browsers and servers is via HTTP, which is stateless. That is, messages between the client and server are completely independent of each other and there is neither notion of sequence or behavior based on previous messages nor relationship with client.

Sessions are the mechanism used by Django for keeping track of the "state" between the site and a particular browser. Sessions store arbitrary data per browser, and have this data available to the site whenever the browser connects. Individual data items associated with the session are then referenced by a "key", which is used both to store and retrieve the data.

The session framework allows to store and retrieve arbitrary data on a per-site-visitor basis. This can provide individual users with a customized experience, based on their previous use of the site, preferences, e.g. hiding warning messages that the user has previously acknowledged next time they visit the site. 

## Enabling sessions

Sessions were enabled automatically when creating a skeleton website. The configuration in **locallibrary/locallibrary/settings.py** file is as shown:

```
INSTALLED_APPS = [
    ...
    'django.contrib.sessions',
    ....

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    ....
```

## Using sessions

Access the `session` attribute of the `request` parameter in the **/locallibrary/catalog/views.py**:

To **get** a session value: `num_visits = request.session.get('num_visits', 1)`

To **set** a session value: `request.session['num_visits'] = num_visits + 1`

To **delete** a session value: `del request.session['num_visit']`

```
def index(request):
    ...
    num_visits = request.session.get('num_visits', 1) # session variable
    request.session['num_visits'] = num_visits + 1
    context = {
        ...
        'num_visits': num_visits, # add number of visits to this view to the context
    }
    return render(request, 'index.html', context=context)
```

Then visit counts can be shown using **/locallibrary/catalog/templates/index.html** by adding the line: `<p>You have visited this page {{ num_visits }} time{{ num_visits|pluralize }}.</p>`

