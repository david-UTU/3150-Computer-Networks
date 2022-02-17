# Assignment 2

## Review Questions

R1. List five nonproprietary Internet applications and the application-layer protocols that they
use.

- Email: SMTP
- File Transfer: FTP
- Remote Terminal Access: Telnet
- Standard Web Access: HTTP
- Internet Telephony: SIP

R2. What is the difference between network architecture and application architecture?

- Network architecture refers to the standard 5 layer system, through which applications get their communication protocols and instructions. Application architecture is dependent on Network architecture, but not vise versa.

R3. For a communication session between a pair of processes, which process is the client and
which is the server?

- Servers sit on standby and wait for a client to send a request.

R4. For a P2P file-sharing application, do you agree with the statement, “There is no notion of
client and server sides of a communication session”? Why or why not?

- No, because all nodes of a peer-to-peer system function as a client and a server. No node is designated as a server or a client. Which node acts as a server and which node acts as a client is dependent on the specific transaction.

R5. What information is used by a process running on one host to identify a process running on
another host?

- The IP address. Port numbers are used for further identification.

R6. Suppose you wanted to do a transaction from a remote client to a server as fast as possible.
Would you use UDP or TCP? Why?

- UDP is faster. TCP has extra guarantees to ensure that the packets have been sent, but UDP does not. Adding this functionality makes TCP slower, at least in the terms of this context, because more than one trip to the client is necessary.

R10. What is meant by a handshaking protocol?

- A set of data packets are sent between two nodes. After these packets have been acknowledged on each end, the transfer of data commences.

R11. Why do HTTP, SMTP, and POP3 run on top of TCP rather than on UDP?

- The guarantee TCP offers that everything has been sent is necessary for the services that these protocols provide. UDP does not have this.

R13. Describe how Web caching can reduce the delay in receiving a requested object. Will Web
caching reduce the delay for all objects requested by a user or for only some of the objects?

- This reduces the amount of information that needs to be requested from a server. This would reduce delay for all objects because there is less traffic.

R17. Print out the header of an e-mail message you have recently received. How many
Received: header lines are there? Analyze each of the header lines in the message.

```html
Received: from esa7.starbucks.iphmx.com (esa7.starbucks.iphmx.com. [216.71.154.37])
        by mx.google.com with ESMTPS id hp24si15544317ejc.879.2022.02.14.07.25.40
        for <dgary416@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);
        Mon, 14 Feb 2022 07:25:41 -0800 (PST)
Received-SPF: pass (google.com: domain of orders@starbucks.com designates 216.71.154.37 as permitted sender) client-ip=216.71.154.37;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@starbucks.com header.s=corp header.b=T1duK9Yw;
       spf=pass (google.com: domain of orders@starbucks.com designates 216.71.154.37 as permitted sender) smtp.mailfrom=orders@starbucks.com;
       dmarc=pass (p=QUARANTINE sp=NONE dis=NONE) header.from=starbucks.com
MIME-Version: 1.0
From: Starbucks Coffee Company <orders@starbucks.com>
To: dgary416@gmail.com
Date: 14 Feb 2022 07:25:31 -0800
Subject: Thank You! Starbucks Card Reload Order L021162J1AQF5482V4MF5L7S40
Content-Type: text/html; charset=utf-8
Content-Transfer-Encoding: base64
Return-Path: orders@starbucks.com 
```

There are 8 headers.

R19. Is it possible for an organization’s Web server and mail server to have exactly the same
alias for a hostname (for example, foo.com )? What would be the type for the RR that contains
the hostname of the mail server?

- Yes, this is possible. The resource record only maps the host name to the IP.

R23. What is an overlay network? Does it include routers? What are the edges in the overlay
network?

- ???

R26. In Section 2.7, the UDP server described needed only one socket, whereas the TCP server
needed two sockets. Why? If the TCP server were to support n simultaneous connections, each
from a different client host, how many sockets would the TCP server need?

- Since TCP has the initial handshake, it requires a socket on each node to perform this. So for each number of clients the UDP server can support, you need that many plus one for the initiation of each TCP client.

## Problems

P1. True or false?
a. A user requests a Web page that consists of some text and three images. For this page,
the client will send one request message and receive four response messages.

- False

b. Two distinct Web pages (for example, www.mit.edu/research.html and
www.mit.edu/students.html ) can be sent over the same persistent connection.

- True

P3. Consider an HTTP client that wants to retrieve a Web document at a given URL. The IP
address of the HTTP server is initially unknown. What transport and application-layer protocols
besides HTTP are needed in this scenario?

- At the transport layer, UDP and TCP are necessary, but I'm a bit confused if I should be saying TCP because that one is being used for HTTP, which it says to exclude from the answer. Idk, Ren, your call.
- At the application layer, DNS are neeeded.

P6c. Can a client open three or more simultaneous connections with a given server?

- No. I wasn't sure based on the text, but according to my internet research, RFC 2616 states that clients should not maintain more than two connections with any proxy or server.

P7. Suppose within your Web browser you click on a link to obtain a Web page. The IP address
for the associated URL is not cached in your local host, so a DNS lookup is necessary to obtain
the IP address. Suppose that n DNS servers are visited before your host receives the IP address
from DNS; the successive visits incur an RTT of RTT1...RTT2... Further suppose that the Web
page associated with the link contains exactly one object, consisting of a small amount of HTML
text. Let RTT denote the RTT between the local host and the server containing the object.
Assuming zero transmission time of the object, how much time elapses from when the client
clicks on the link until the client receives the object?

- For TCP, you have double RTT for the starting point, and then every subsequent RTT gets added on for the total amount of time.
- In math terms, 2*(RTT-1) + RTT-2 + RTT-3 ... RTT-n

P13. What is the difference between MAIL FROM : in SMTP and From : in the mail message
itself?

- The From section is just the text representing the sender of the original message.
- The MAIL FROM is attached on by the client that identifies the original sender.

P14. How does SMTP mark the end of a message body? How about HTTP? Can HTTP use the
same method as SMTP to mark the end of a message body? Explain.

- HTTP has a specific header that indicates the length of a messsage, but SMTP simply has a line with a period in it to indicate the end of a message. So no, HTTP cannot follow the same system that SMTP is using.

P18d. Use nslookup to find a Web server that has multiple IP addresses. Does the Web server
of your institution (school or company) have multiple IP addresses?

```markdown
Server:         144.38.53.11
Address:        144.38.53.11#53

Name:   dixie.edu
Address: 144.38.31.70
```

- Yes, our insititution does have multiple addresses.

P20. Suppose you can access the caches in the local DNS servers of your department. Can you
propose a way to roughly determine the Web servers (outside your department) that are most
popular among the users in your department? Explain.

- For each unique instance of reaching a web server being cached in the local DNS server, a record will be maintained. Therefore, the address that is cached the most, is likely to be the most popular.
