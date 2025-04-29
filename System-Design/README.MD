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
    - Balances the load bases on the requests per user and caching so that one user within specific period of time will send to same machine

### Change the Color to Terminal Folder

- PS1="\[\e[36m\]\w\[\e[0m\] \[\e[33m\]\$\[\e[0m\] "
- vim ~/.bashrc
- source ~/.bashrc

