# IP Classes

## Subnet Size

- The bigger the host portion of the network, the more hosts we can
    have
- If the subnet mask is `/8`, we have 24 bits available to allocate to
    hosts, for example
- Unfortunately, when `IPv4` was created, the designers didn't realise
    how big the internet was going to get, and they didn't create a
    big enough address space. The long term solution to this, is
    `IPv6` which has a much bigger address space.

| Class | Mask | Valid address          | Nets | Hosts   |
| :---: | ---- | :--------------------- | :--- | :------ |
| `A`   | 8    | `1.0.0.0`, `126.0.0.0` | 126  | 1677214 |
| `A`   | 

## Class A

- Assigned to networks with a very large number of hosts.
- The first bit in a class `A` address is always set to zero.
- `0.0.0.0/8` is reserved and signifies *this network*
- `0.0.0.1` to `0.255.255.255` are not valid host addresses.
- `127.0.0.0/8` in the Class `A` is reserved as the *loopback* address
    for testing the local computer.
- `127.0.0.1` to `127.255.255.255` are not valid host addresses.
- This wipes out 33554428 ($2 * (2^{8 * 3} - 1) - 2$) addresses from
    the global address pool.
