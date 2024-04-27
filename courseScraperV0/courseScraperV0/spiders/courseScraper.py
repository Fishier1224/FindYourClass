import scrapy
import csv

class CourseSpider(scrapy.Spider):
    name = "courses"

    def start_requests(self):
        url = 'https://catalogue.usc.edu/preview_program.php?catoid=18&poid=25219&returnto=7464'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract course names
        courses = response.css('.acalog-course a::text').getall()

        # Write course names to CSV file
        with open('mathematicsBS.csv', 'w', newline='') as csvfile:
            fieldnames = ['Course Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for course in courses:
                writer.writerow({'Course Name': course.strip()})

