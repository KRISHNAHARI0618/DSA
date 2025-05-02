# System Design Concepts Need To learn 

## What is system design

- System Design refers a process for defining the architecture,components,modules,interfaces,data for a system to satisfy the business requirement
- Takes Decision how a system will work and what components it will interact
- Make sure system is Highly Available,Scalable,Consistent,reliable etcc..
- Provides High ThroughPut, Low Latency

- **Throughput**
  - Specific Period of Time = no of process or tasks or amount of data transfered in time
  - **In Networking**: Throughput is typically the rate at which data is transferred from one point to another, usually measured in bits per second (bps), kilobits per second (kbps), or megabits per second (Mbps).
  - **In Computing**: Throughput can refer to the number of operations (like database transactions or requests) completed in a given time frame.
- **Latency**
  - Delay in responce or time taken to perform one single operation 
  - It measures responce time of the system within network
  - **In Networking**: 
    - latency is the timetaken to transfer one data packet from sender to receiver. usually measure in milliseconds
  - **In Computing**:
    - Time taken by the system to give responce to users based on the input provided
    - Time taken to respond the application
- **Scaling Capabilities**
  - When the users / requests increase one sysem can crash if there are no enought resources available so scaling comes into play
  - There are two types of scaling
    - 1: *Horizontal Scaling*
      - Increase the machines as per scalability
      - Required Load Balancing to distribute the traffic
      - The System is resilient
      - I/O Communication --> Calls over Remote -> Network Calls
      - Data Consistency will be minor challenge
      - Scales as the users Increases
    - 2: *Vertical Scaling*
      - Increaase the resources like cpu & memory
      - Not Required Load Balancing
      - The System is not resilient
      - Data Consisteny will not be issue
      - Single Point of Failure
      - There should be a Limit in Hardware
- **Consistent Hashing**
  - *Load Balancing*
    - Balances the load bases on the requests per user and caching so that one user within specific period of time will send to same machine.

### Messaging Queues:
- Messaging queue is a components where it takes requests/tasks and process and will send to particular servers and gets acknowledged 
- if it has not received any requests within some time it feels sever is not ready and send the requests to another active server
- Servers are processing jobs in parallel.
- A server can crash. The jobs running on the crashed server still needs to get processed.
- A notifier constantly polls the status of each server and if a server crashes it takes ALL unfinished jobs (listed in some database) and distributes it to the rest of the servers.
- Because distribution uses a load balancer (with consistent hashing) duplicate processing will not occur as job_1 which might be processing on server_3 (alive) will land again on server_3, and so on.
- This "notifier with load balancing" is a "Message Queue".