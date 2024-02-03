def capture_social_auth_data(backend, user, request, response, details ,*args, **kwargs):
    """
    Capture Google OAuth2 data and store user-related information in the session.
    
    """
    # backend = backend

    print('Response:', response)
    print('Details:', details)

    if backend and backend.name == 'google-oauth2':
        # If the backend is GoogleOAuth2
        google_data = {
            'uid': response.get('sub'),
            'email': response.get('email'),
            'uname': response.get('given_name'),
            # Add other Google-related data as needed
        }
        request.session['social_auth_google-oauth2'] = google_data

        # # Additionally, store user-related data in the session
        # strategy.request.session['user_id'] = user.id
        # strategy.request.session['user_email'] = user.email
        # strategy.request.session['user_fname'] = user.fname