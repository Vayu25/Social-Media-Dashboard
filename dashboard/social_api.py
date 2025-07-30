from datetime import datetime

def fetch_mock_twitter_posts(username):
    # Simulate Twitter API response
    return [
        {
            'platform': 'Twitter',
            'username': username,
            'content': '🚀 Starship launch successful!',
            'timestamp': datetime.now().strftime('%d %b %Y %H:%M')
        },
        {
            'platform': 'Twitter',
            'username': username,
            'content': 'Python 3.13 beta is out now.',
            'timestamp': datetime.now().strftime('%d %b %Y %H:%M')
        }
    ]

def fetch_mock_facebook_posts(username):
    # Simulate Facebook API response
    return [
        {
            'platform': 'Facebook',
            'username': username,
            'content': 'Meta Connect 2025 announced!',
            'timestamp': datetime.now().strftime('%d %b %Y %H:%M')
        }
    ]
