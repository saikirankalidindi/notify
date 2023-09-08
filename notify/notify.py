from pushbullet import Pushbullet

# Replace 'YOUR_ACCESS_TOKEN' with your actual Pushbullet access token
pb = Pushbullet('o.ZK1Bl03IqlE9w08Nj5X2YWD1FE35HZG2')

class push:
    def send_body(self,title,message='program completed'):
        pb.push_note(f'{title}',f'{message}')

send = push()