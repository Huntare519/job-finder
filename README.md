# job-finder

Job Finder is a solution to the monotony of checking countless company career pages every Fall semester. This repo programmatically
searches through your defined career websites for your defined keywords. When found, you will recieve an email with a link to the job.

## Configuration

An example of the configuration. You can define as many keywords as you want.

```yaml
- name: Rivian
  keywords: [Intern, Interns, Co-op]
  job-posting-tag: h6
  job-board-type: custom
  url: https://rivian.com/careers
```

Currently, the code works best with:

1. [Lever](https://www.lever.co)
2. [Greenhouse](https://www.greenhouse.io)
3. [Tesla](#) (in dev)

More compatibility is forthcoming.

## Fun Things

Sometimes, as it was the case with Rivian, I created custom logic to scrape their website. However, I noticed that in the HTML, each job posting just linked to a greenhouse board. Scraping the greenhouse board is faster and easier, since I already wrote that logic and it runs cleanly and smoothly. The lesson learned from the Rivian experience was to **check the HTML before writing custom logic**.

## Ways to Make Job-Finder Better (Forthcoming)

- discover ways to make the HTML email more appealing, and work with light and dark email clients
- add compatibilty to more websites other than just greenhouse and lever
  - i.e. tesla, pwc, etc.
- research ways for this script to run async on mondays / tuesdays
  - aws lamdbda, azure, raspberry pi plugged into my computer at school, etc.
- setup github repo and make it private
