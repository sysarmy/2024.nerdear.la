# How does the `templates/` directory work

(copy-pasted from root README.md)

Every file inside `templates/` (except `base.html`) is rendered using render_template in an specific route defined in `routes.py`.
Each file inherits from `base.html`, and uses the components in `components/` using `{% include "components/component_name_here.html" %}`

**This is done for the purpose of clean and tidy code**

An example of a component could be:

```html
<!-- This file holds the section that talks about the speakers -->
<section id="speakers">
	<!-- Get the css file using jinja-html syntax -->
	<link rel="stylesheet" href="{{ url_for('static', filename='css/speakers.css') }}" />

	<!-- Main content of the html -->
	<div class="container">
		<h1>Nuestros speakers</h1>
		<div>
			<p>Our speakers are great because...</p>
		</div>
	</div>

	<!-- Get the javascript file using jinja-html syntax -->
	<script src="{{ url_for('static', filename='js/speakers.js') }}"></script>
</section>
```
