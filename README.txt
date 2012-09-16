=========
httperfpy
=========

A python port of `httperfrb<http://github.com/rubyops/httperfrb>`.

Built and tested using: 

        $ python --version
        Python 2.7.3

        $ uname -s -r -m
        Linux 3.2.0-29-generic x86_64 



Installing 'httperf'
====================

Requires httperf, of course...

Mac
------

    sudo port install httperf

Debian / Ubuntu
---------------

    sudo apt-get install httperf

Redhat / CentOS
---------------

    sudo yum install httperf
    
My 'httperf'
------------

** This is required for proper verbose handling. **

See: `httperf-0.9.1 with individual connection times<http://www.rubyops.net/2012/08/13/httperf-0_9_1_with_individual_connection_times>`.


Installation / Setup
====================

Perferred Method
----------------

        $ sudo pip install httperfpy

See: http://pypi.python.org/pypi/httperfpy/

From Source
-----------

Simply clone code and add checkout location to your PYTHONPATH.

Running tests...
----------------

1. sudo apt-get install python-unit
2. git clone https://github.com/jmervine/httperfpy.git
3. cd httperfpy
4. ./scripts/unit


Usage
-----

        #!/usr/bin/env python
        from httperf import Httperf
        
        perf = Httperf(server="www.example.com", 
                        port=8080,
                        num_conns=100)
        # replace dashes ("-") with underscores ("_") in httperf options

        perf.parser = True

        results = perf.run()

        print results["connection_time_avg"] + " is avg"
        print results["connection_time_max"] + " is max"


You can use `Httperf.display_options` to print a list of all available options.


Stand-alone parser...
---------------------

        #!/usr/bin/env python
        from httperf import HttperfParser
        
        results = HttperfParser.parse(httperf_result_string)
        print results["connection_time_avg"] + " is avg"
        print results["connection_time_max"] + " is max"
      


Parser Keys: 
------------

    - command
    - max_connect_burst_length
    - total_connections
    - total_requests
    - total_replies
    - total_test_duration
    - connection_rate_per_sec
    - connection_rate_ms_conn
    - connection_time_min
    - connection_time_avg
    - connection_time_max
    - connection_time_median
    - connection_time_stddev
    - connection_time_connect
    - connection_length
    - request_rate_per_sec
    - request_rate_ms_request
    - request_size
    - reply_rate_min
    - reply_rate_avg
    - reply_rate_max
    - reply_rate_stddev
    - reply_rate_samples
    - reply_time_response
    - reply_time_transfer
    - reply_size_header
    - reply_size_content
    - reply_size_footer
    - reply_size_total
    - reply_status_1xx
    - reply_status_2xx
    - reply_status_3xx
    - reply_status_4xx
    - reply_status_5xx
    - cpu_time_user_sec
    - cpu_time_system_sec
    - cpu_time_user_pct
    - cpu_time_system_pct
    - cpu_time_total_pct
    - net_io_kb_sec
    - net_io_bps
    - errors_total
    - errors_client_timeout
    - errors_socket_timeout
    - errors_conn_refused
    - errors_conn_reset
    - errors_fd_unavail
    - errors_addr_unavail
    - errors_ftab_full
    - errors_other
         

