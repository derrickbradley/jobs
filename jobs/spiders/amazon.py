import json
import scrapy

class AmazonSpider(scrapy.Spider):
  name = 'amazon'
  int_offset = 0
  offset = 0
  amzn_base_url = "https://www.amazon.jobs/en/search?base_query=&result_limit=200&offset={}&sort=recent&category%5B%5D=software-development&animate=false".format(int_offset)
  start_urls = [amzn_base_url]
  download_delay = 2.5

  def parse(self, response):
    i = 0
    
    jobs = json.loads(response.body)
    job_count = jobs.get('hits')
    
    print job_count
    
    for job in jobs.get('jobs', []):
      i += 1
      print i
      
      print job.get('title')
      
      # yield {
      #   'title': job.get('title'),
      #   'business_category': job.get('business_category'),
      #   'job_category': job.get('job_category'),
      #   'company_name': job.get('company_name'),
      #   'description': job.get('description'),
      #   'preferred_qualifications': job.get('preferred_qualifications'),
      #   'basic_qualifications': job.get('basic_qualifications'),
      #   'country_code': job.get('country_code'),
      #   'state': job.get('state'),
      #   'job_path': job.get('job_path'),
      # }
    
    offset = 0
    
    while offset <= job_count:
      yield scrapy.Request(self.amzn_base_url.format(offset))
      offset += 200
      print(offset)
      