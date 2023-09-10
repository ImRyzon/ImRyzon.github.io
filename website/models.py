from django.db import models


BADGE_CHOICES = (
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('Python', 'Python'),
    ('JavaScript', 'JavaScript'),
    ('Java', 'Java'),
    ('C++', 'C++'),
    ('C#', 'C#'),
    ('SQL', 'SQL'),
    ('PHP', 'PHP'),
    ('Flask', 'Flask'),
    ('Django', 'Django'),
    ('React.js', 'React.js'),
    ('Cybersecurity', 'Cybersecurity'),
    ('Algorithms', 'Algorithms'),
    ('Data Structures', 'Data Structures'),
    ('Competitive Programming', 'Competitive Programming'),
    ('CTF', 'CTF'),
    ('Web', 'Web'),
    ('CS50', 'CS50'),
    ('AI', 'AI'),
    ('GUI', 'GUI'),
    ('BOT', 'BOT')
)


class Badge(models.Model):
    badge = models.CharField(max_length=32, default=None, choices=BADGE_CHOICES, unique=True)

    def __str__(self):
        return f"{self.badge}"
    

class Comment(models.Model):
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True, default="")
    content = models.TextField(max_length=1024, default=None)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_reply = models.BooleanField(default=False)
    replies = models.ManyToManyField("self", blank=True, symmetrical=False, default=None)

    def __str__(self):
        return f"Comment ID#{self.id} by \"{self.first_name} {self.last_name}\""
    
        
    def serialize(self):
        return {
            "id" : self.id,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "content" : self.content,
            "date" : self.date.strftime("%b %d %Y, %I:%M %p"),
            "is_active" : self.is_active,
            "is_reply" : self.is_reply,
            "replies" : [reply.id for reply in self.replies.all()]
        }


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    image_path = models.CharField(max_length=64)
    badges = models.ManyToManyField(Badge, related_name="projects", default=None, symmetrical=False)
    in_progress = models.BooleanField(default=True)
    link = models.CharField(max_length=1024, default="", null=True, blank=True)

    def __str__(self):
        return f"Project #{self.id}: {self.title}"
    
    def serialize(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "image_path" : self.image_path,
            "badges" : [badge.badge for badge in self.badges.all()],
            "in_progress" : self.in_progress,
            "link" : self.link
        }


class Blog(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    approx_length_min = models.IntegerField(default=5)
    image_path = models.CharField(max_length=64)
    comments = models.ManyToManyField(Comment, blank=True, related_name="blogs")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Blog #{self.id}: {self.title}"
    
    def serialize(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "content" : self.content,
            "date" : self.date.strftime("%b %d %Y"),
            "approx_length_min" : self.approx_length_min,
            "image_path" : self.image_path,
            "comments" : [comment.id for comment in self.comments.all()],
            "is_active" : self.is_active
        }
