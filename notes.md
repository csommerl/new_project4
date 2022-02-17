        <div id="new-post-form" class="form-group card text-dark bg-light m-3 mx-auto" style="width: 50rem;">
            <form action="/new-post-submit" method="POST">
                {% csrf_token %}
                <div>
                    <p>{{form.as_p}}</p>
                </div>
                <input class="btn btn-primary" type="submit" value="Submit">
            </form>
        </div>