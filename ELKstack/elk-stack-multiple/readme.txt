.
├── data
│   ├── apache_logs.txt
│   ├── data.csv
│   └── data-json.log
├── docker-compose.yml
├── filebeat
│   └── filebeat.yml
├── logs
│   └── python_logs.log
├── logstash
│   ├── config
│   │   ├── logstash.yml
│   │   └── pipelines.yml
│   └── pipeline
│       ├── logstash-apache.conf
│       ├── logstash-python-log.conf
│       └── logstash-csv.conf
├── README.md
└── send_logs.py