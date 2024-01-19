class Blog:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.posts = []
        
    def __repr__(self):
        return f'{self.title} by {self.author} ({len(self.posts)} post{"" if len(self.posts) <= 1 else "s"})'
    
    def create_post(self, title, content):
        pass
    
    def json(self):
        pass
    