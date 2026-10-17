from django.db import models
import random

# Create your models here.
class MadLib(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    adjective = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    animal = models.CharField(max_length=100)
    feeling = models.CharField(max_length=100)
    verb = models.CharField(max_length=100)
    story_text = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def create_story(self):
        stories = [
            f"Once upon a time, {self.name} lived in {self.place}, where there was a {self.adjective} {self.color} {self.animal}. It felt very {self.feeling} and decided to {self.verb}.", 
            f"One day, {self.name} went to {self.place} and saw a {self.adjective} {self.color} {self.animal}. It was feeling very {self.feeling} and decided to {self.verb}.",
            f"Long ago, {self.name} traveled to {self.place} and encountered a {self.adjective} {self.color} {self.animal}. It was feeling quite {self.feeling} and chose to {self.verb}.",
            f"In a distant land, {self.name} discovered a {self.adjective} {self.color} {self.animal} in {self.place}. It was feeling very {self.feeling} and decided to {self.verb}.",
            f"During an adventure, {self.name} visited {self.place} and met a {self.adjective} {self.color} {self.animal}. It was feeling extremely {self.feeling} and opted to {self.verb}.",
            f"One sunny day, {self.name} went to {self.place} and found a {self.adjective} {self.color} {self.animal}. It was feeling quite {self.feeling} and decided to {self.verb}.",
            f"While exploring {self.place}, {self.name} stumbled upon a {self.adjective} {self.color} {self.animal}. It was feeling very {self.feeling} and chose to {self.verb}.",
            f"On a magical journey, {self.name} arrived at {self.place} and encountered a {self.adjective} {self.color} {self.animal}. It was feeling very {self.feeling} and decided to {self.verb}.",
            f"During a whimsical adventure, {self.name} visited {self.place} and saw a {self.adjective} {self.color} {self.animal}. It was feeling very {self.feeling} and decided to {self.verb}.",
            f"{self.adjective} {self.name} had a {self.place} and at this {self.place}, they had a {self.color} {self.animal}. It was feeling very {self.feeling} and they decided to {self.verb}.",
            f"There once was a {self.color} {self.animal} that lived in {self.place}. It was very {self.adjective} and often felt {self.feeling}. One day, it decided to {self.verb} with its friend, {self.name}.",
            f"{self.name} was a {self.adjective} person who loved to visit {self.place}. One day, they saw a {self.color} {self.animal} that was feeling very {self.feeling}. They decided to {self.verb} together.",
            f"{self.name} lived in {self.adjective} {self.place} and had a pet {self.color} {self.animal}. One day, the {self.animal} was feeling very {self.feeling}, so they decided to {self.verb} to cheer it up.",
            f"There was a {self.color} {self.animal} that lived in {self.adjective}{self.place} named {self.name}. It was very {self.feeling}. One day, it decided to {self.verb} to make new friends.",
            f"{self.name} was a {self.adjective} adventurer who traveled to {self.place}. There, they met a {self.color} {self.animal} that was feeling very {self.feeling}. Together, they decided to {self.verb}.",
            f"Interesting choices: {self.name}, {self.place}, {self.adjective}, {self.color}, {self.animal},{self.feeling}, {self.verb}",
        ]
        self.story_text = random.choice(stories)
        return self.story_text