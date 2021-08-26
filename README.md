# Network
Design a Twitter-like social network website for making posts and following users.
https://cs50.harvard.edu/web/2020/projects/4/network/

# Getting Started
1. Download the distribution code from https://cdn.cs50.net/web/2020/spring/projects/4/network.zip and unzip it.
2. In your terminal, `cd` into the `project4` directory.
3. Run `python manage.py makemigrations network` to make migrations for the network app.
4. Run `python manage.py migrate` to apply migrations to your database.

# Understanding
In the distribution code is a Django project called `project4` that contains a single app called `network`, structured similarly to Project 2’s `auctions` app.

First, open up `network/urls.py`, where the URL configuration for this app is defined. Notice that we’ve already written a few URLs for you, including:
1. a default `index` route,
2. a `/login route`,
3. a `/logout` route, and
4. a `/register` route.

Take a look at `network/views.py` to see the views that are associated with each of these routes.
1. The `index` view for now returns a mostly-empty `index.html` template.
2. The `login_view` view renders a login form when a user tries to `GET` the page. When a user submits the form using the `POST` request method, the user is authenticated, logged in, and redirected to the index page.
3. The `logout_view` view logs the user out and redirects them to the index page.
4. Finally, the `register` route displays a registration form to the user, and creates a new user when the form is submitted. All of this is done for you in the distribution code, so you should be able to run the application now to create some users.

Run `python manage.py runserver` to start up the Django web server, and visit the website in your browser. Click “Register” and register for an account. You should see that you are now “Signed in as” your user account, and the links at the top of the page have changed. How did the HTML change? Take a look at `network/templates/network/layout.html` for the HTML layout of this application. Notice that several parts of the template are wrapped in a check for if `user.is_authenticated`, so that different content can be rendered depending on whether the user is signed in or not. You’re welcome to change this file if you’d like to add or modify anything in the layout!

Finally, take a look at `network/models.py`. This is where you will define any models for your web application, where each model represents some type of data you want to store in your database. We’ve started you with a `User` model that represents each user of the application. Because it inherits from `AbstractUser`, it will already have fields for a `username`, `email`, `password`, etc., but you’re welcome to add new fields to the `User` class if there is additional information about a user that you wish to represent. You will also need to add additional models to this file to represent details about posts, likes, and followers. Remember that each time you change anything in `network/models.py`, you’ll need to first run `python manage.py makemigrations` and then `python manage.py migrate` to migrate those changes to your database.

# Specification
Using Python, JavaScript, HTML, and CSS, complete the implementation of a social network that allows users to make posts, follow other users, and “like” posts. You must fulfill the following requirements:

## Create Models
- [x] Create models for:
    - [x] Post
    - [x] Like
        - [x] different `related_name` needed for `liked_post` and `liker`?
        - maybe should have default for like_status set to false?
        - like status is being used so that no likes are deleted, and so the database keeps a history of all likes
        - [x] how to get timestamp of both original like and unlike?
    - [x] Follower
        - maybe different related_name needed?
- Mine:
    - [x] Add string representations for each
    - [x] Update admin interface for each

## New Post
- [x] Users who are signed in should be able to write a new text-based post by filling in text into a text area and then clicking a button to submit the post.
    - [x] The screenshot at the top of this specification shows the “New Post” box at the top of the “All Posts” page. You may choose to do this as well, or you may make the “New Post” feature a separate page.
- [x] Mine:
    - [x] create limit of character input
    - [x] redirect after posting
    - [x] tidy up design of form
    - [x] add csrf functionality
        - https://docs.djangoproject.com/en/3.2/ref/csrf/
        - https://github.com/ghrust/cs50w-project4-network/
        - https://github.com/EgidioHPaixao/web50-projects-2020-x-network/blob/master/network/static/network/index.js
    - [x] make it so that the form appears only when logged in
    - [x] add messages, with successful post and no content post
    - [x] Use django form instead, especially for csrf?
    - cf. https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
    - https://docs.djangoproject.com/en/3.2/topics/forms/#form-rendering-options

## All Posts
- [x] The “All Posts” link in the navigation bar should take the user to a page where they can see all posts from all users,
    [x] with the most recent posts first.
- [x] Each post should include:
    - [x] the username of the poster,
    - [x] the post content itself,
    - [x] the date and time at which the post was made, and
    - [x] the number of “likes” the post has (this will be 0 for all posts until you implement the ability to “like” a post later).
- [ ] Mine:
    - [ ] Update automatically after submitting new post
    - [ ] update what to dowhen there are no posts
    - [ ] reduce redundancy with profile page posts display
    - [ ] display when it was edited
    - [x] update formatting of likes

## Profile Page
- [ ] Clicking on a username should load that user’s profile page. This page should:
    - [ ] Add link to each username in js loadpost function
    - [ ] Display the number of followers the user has, as well as the number of people that the user follows.
    - [ ] Display all of the posts for that user, in reverse chronological order.
        - [ ] display likes
    - [ ] For any other user who is signed in
        - [ ] this page should also display a “Follow” or “Unfollow” button
        - [ ] that will let the current user toggle whether or not they are following this user’s posts.
            1. ~~NO: use fetch without boolean
                - unclear how to use fetch to delete an entry
                - if deleting/creating database instance of Follow, then two different fetch requests need to be used:
                    1. follow:
                    2. unfollow:~~
            2. YES: maybe fetch doesn't need to used at all: clicking teh button should just run a function in view that deletes or creates instance
                - problem: unclear what to write, without using fetch, in js to run a view function
                - Answer: https://stackoverflow.com/a/58122376
                - cf. https://stackoverflow.com/questions/15341285/how-do-i-call-a-django-function-on-button-click
                - and cf. https://stackoverflow.com/questions/17599035/django-how-can-i-call-a-view-function-from-template/19761466#19761466
            3. ~~NO use fetch with boolean~~
        - [ ] should refresh after clicking:
            - NOT USED: javascript event listener
            - USED: alternatively could use a redirect in python view
        - [ ] Note that this only applies to any “other” user: a user should not be able to follow themselves.
- [ ] Mine:
    - [ ] Reduce redundancy with all posts
    - [ ] Change browser bar title
    - [ ] add try except for non-existent users
    - [ ] update what to dowhen there are no posts
    - [ ] add styling for follow data

## Following
- [ ] The “Following” link in the navigation bar should take the user to a page where they see all posts made by users that the current user follows.
- [ ] This page should behave just as the “All Posts” page does, just with a more limited set of posts.
- [ ] This page should only be available to users who are signed in.
- [ ] Mine:
    - [ ] Fix follow model:
        - [ ] what to do when unfollowing: boolean or delete entry?
        - [ ] how to ensure that there can be only one follow instance for a given follower/followed?
        - [ ] make sure to fix for when no users are followed

## Pagination
- [x] On any page that displays posts, posts should only be displayed 10 on a page.
    - [x] If there are more than ten posts, a “Next” button should appear to take the user to the next page of posts (which should be older than the current page of posts).
    - [x] If not on the first page, a “Previous” button should appear to take the user to the previous page of posts as well.
    - [x] See the Hints section for some suggestions on how to implement this.
- [x] Mine:
    - [x] style it better, with Bootstrap / Javascript

## Edit Post
- [ ] Users should be able to click an “Edit” button or link on any of their own posts to edit that post.
    - [ ] When a user clicks “Edit” for one of their own posts, the content of their post should be replaced with a textarea where the user can edit the content of their post.
- [ ] The user should then be able to “Save” the edited post.
    - [ ] Using JavaScript, you should be able to achieve this without requiring a reload of the entire page.
- [ ] For security, ensure that your application is designed such that it is not possible for a user, via any route, to edit another user’s posts.

## “Like” and “Unlike”
- [x] Users should be able to click a button or link on any post to toggle whether or not they “like” that post.
    - [x] unliking not working sometimes, e.g., after refreshing
        - maybe try other users
        - use `POST` method?
        - problem was duplicate likes, it couldn't tell which to change
- [x] Using JavaScript, you should asynchronously let the server know to update the like count (as via a call to `fetch`) and then update the post’s like count displayed on the page, without requiring a reload of the entire page.
- [ ] Mine:
    - [x] Add to all posts: the number of “likes” the post has (this will be 0 for all posts until you implement the ability to “like” a post later).
    - [x] Fix like model:
        - [x] what to do when unliking: boolean or delete entry?
        - [x] how to ensure that there can be only one lilke instance for a given user/post?
    - [ ] **prevent users who are not logged on from clicking "Like"**
    - [x] unliking not working sometimes
    - [ ] remove `csrf exempt`?

## My Possible Features
- [ ] Use React?
- [ ] Use Github Issues
- [ ] Use Github Actions, other testing
- [ ] Add bootstrap
- [ ] after clicking follow button, only refresh button without refreshing whole page
    - problem: the button works by a link in the template to a python function
        - which must return a httpresponse, and hence to a page
    - possible solution: ?????
    - make sure that it only works when user is authenticated
    - old in template: `<button id="follow-button" class="btn-primary" onclick="location.href='{% url 'follow-or-unfollow' username %}'"></button>`
- [ ] add id to each post in all post, profile post, etc.
    - this will help maybe with editing posts
- [ ] refresh of all posts after submitting new one: add to js new post function instead of at the top
- [ ] Instead of deleting from the database unfollows & unlikes, keep track of them --> presumably by using a boolean
- [ ] add csrf protection to follow & unfollow
- [ ] check best place to link to network.js: layout or individual pages?
- [ ] add better/more browser bar and top of page headings

# Hints
- [x] For examples of JavaScript `fetch` calls, you may find some of the routes in Project 3 useful to reference.
- [x] You’ll likely need to create one or more `models` in `network/models.py` and/or modify the existing `User` model to store the necessary data for your web application.
- [x] Django’s [`Paginator`](https://docs.djangoproject.com/en/3.2/topics/pagination/) class may be helpful for implementing pagination on the back-end (in your Python code).
- [x] Bootstrap’s [`Pagination`](https://getbootstrap.com/docs/4.0/components/pagination/) features may be helpful for displaying pages on the front-end (in your HTML).

# Boostrap
- https://getbootstrap.com/docs/4.0/utilities/spacing/
- https://getbootstrap.com/docs/5.0/components/card/
- https://getbootstrap.com/docs/5.0/utilities/text/