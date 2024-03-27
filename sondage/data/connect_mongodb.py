from django.core.management.base import BaseCommand
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Command(BaseCommand):
    help = 'Connect to MongoDB'

    def handle(self, *args, **options):
        print("hey")
        uri = "mongodb+srv://rawanatwe:dB1XUvmxiphGlJzQ@cluster1.7b86nya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            self.stdout.write(self.style.SUCCESS("Pinged your deployment. You successfully connected to MongoDB!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error connecting to MongoDB: {e}"))

if __name__ == "__main__":
    Command().handle()