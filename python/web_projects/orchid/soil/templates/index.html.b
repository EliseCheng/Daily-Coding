{% load bootstrap3 %}

{# Display a form #}

<form action="/url/to/submit/" method="post" class="form">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
        <button type="submit" class="btn btn-primary">
            {% bootstrap_icon "star" %} Submit
        </button>
    {% endbuttons %}
</form>
