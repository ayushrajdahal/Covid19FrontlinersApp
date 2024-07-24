# Blog Project

This is a Django-based blog project with a marketing component and a posts component. The project is structured to include backend services, static files, and templates for rendering the frontend.

## Getting Started

### Prerequisites

- Python 3.7+
- Django 3.0.5
- Other dependencies listed in [`requirements.txt`]("/Users/x/projects/django-blog/requirements.txt")

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/ayushrajdahal/django-blog.git
   cd django-blog
   ```

2. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Apply the migrations:

   ```sh
   python manage.py migrate
   ```

4. Run the development server:
   ```sh
   python manage.py runserver
   ```

### Configuration

- **Settings**: Configuration settings are located in [`blogproject/settings.py`]("/Users/x/projects/django-blog/blogproject/settings.py").
- **URLs**: URL routing is managed in [`blogproject/urls.py`]("/Users/x/projects/django-blog/blogproject/urls.py").

### Running Tests

To run the tests, use the following command:

```sh
python manage.py test
```

## Project Components

### Backend

- **Custom Azure**: Custom backend services are implemented in [`backend/custom_azure.py`](backend/custom_azure.py).

### Marketing

- **Models**: Defined in [`marketing/models.py`](marketing/models.py).
- **Views**: Defined in [`marketing/views.py`](marketing/views.py).
- **Forms**: Defined in [`marketing/forms.py`](marketing/forms.py).
- **Admin**: Admin configurations are in [`marketing/admin.py`](marketing/admin.py).

### Posts

- **Models**: Defined in [`posts/models.py`](posts/models.py).
- **Views**: Defined in [`posts/views.py`](posts/views.py).
- **Forms**: Defined in [`posts/forms.py`](posts/forms.py).
- **Admin**: Admin configurations are in [`posts/admin.py`](posts/admin.py).
- **Twitter Integration**: Implemented in [`posts/twitter.py`](posts/twitter.py).

### Static Files

Static files are located in the `static_in_env` directory, which includes:

- Contact form scripts
- Fonts
- Images
- JavaScript files
- Stylesheets

### Templates

HTML templates are located in the `templates` directory and include:

- `404.html`
- `about.html`
- `account/`
- `base.html`
- `blog.html`
- `faq.html`
- And more...

## Deployment

Deployment configurations are specified in:

- `Procfile`
- `runtime.txt`

## License

[MIT License](LICENSE)

---

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.
