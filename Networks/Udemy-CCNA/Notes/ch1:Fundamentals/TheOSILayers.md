# The OSI Layers

## L7 - The Application Layer

- Provides network services to the applications of the user
- Establishes the availability of intended communication partners
- It then synchronizes and establishes agreement on procedures for
    error recovery and control of data integrity.

## L6 - The Presentation Layer

- Ensures that the information that is sent at the application layer
    of one system is readable by the application layer of another
    system.
- Can translate among multiple data formats using a common format (ex.
    computers with different encoding schemes)

## L5 - The Session Layer

- Establishes, manages and terminates sessions between two
    communicating hosts.
- It also synchronizes dialog between the presentation layers of the
    two hosts and manages their data exchange.
- It also offers efficient data transfer, CoS (Class of Service) and
    exception reporting of upper layer problems.

## L4 - The Transport Layer

- Main characteristics: whether TCP or UDP transport is used
    and the port number.
- Defines services to segment, transfer and reassemble the data for
    individual communications between the end devices.
- It breaks down large files into smaller segments that are less
    likely to incur transmission problems.

## L3 - The Network Layer

- Important information: the source and destination IP addresses.
- Provides connectivity and path selection between two host systems
    that may be located on geographically separated networks.
- Is the layer that manages the connectivity of hosts by providing
    logical addressing

## L2 - The Data-Link Layer

- Important information: the source and destination layer 2 addresses
- Defines how data is formatted for transmission and how access to
    physical media is controlled.
- It also typically includes error detection and correction to ensure
    a reliable delivery of the data.
- If it's not Ethernet, which other technologies could be used?

## L1 - The Physical Layer

- It concerns the physical components of the network
- Enables bit transmission between end devices.
- Defines specifications needed for activating, maintaining and
    deactivating the physical link between end devices.
- Voltage levels, physical data rates, maximum transmission distances,
    physical connectors, etc.
