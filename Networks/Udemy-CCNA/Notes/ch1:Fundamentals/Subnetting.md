# Subnetting

*Classless Inter-Domain Routing* (`CIDR`) was introduced in 1993 to
alleviate waste of global address space with classfull addresses.
Companies can now be allocated an address range which more closely
matches their needs and does not waste addresses

### Benefits of `CIDR`:

- By removing the fixed `/8`, `/16` and `/24` requirements for the
    address classes, allows them to be *subnetted* into smaller ones.
- Aggregated blocks of networks can be advertised on the Internet.

### Route Summarisation Benefits

- `ISP A` doesn't know about all 256 `/24` networks reachable in `ISP B`
- It only has the single `175.11.0.0/16` summary route.
- This reduces the size of `ISP A`'s routing table, using less memory
- If and individual link goes down in `ISP B`, it has no impact on
    `ISP A`. The single summary route does not change.
- This restricts issues to the local part of the network and reduces
    CPU load.

---

## Borrowing Host Bits

- To subnet the network into smaller subnets, we need to borrow host
    bits and add them to the network portion of the address.
- The network address line always moves to the right when we subnet
- The further to the right we go, the more subnets we'll have of that
    size but less hosts.

## Calculating the Number of Networks and Hosts

- Available subnets: $2^{\text{bits borrowed}}$
- Hosts on different subnets need to go via a router if they want to
    communicate with each other. 
- Available hosts: $2^{\text{host bits}} - 2$
- We substract 2 because the network address and broadcast address
    cannot be assigned to hosts.
- The amount of hosts will depend on the subnet size and it's equal
    for any IP class.
- In the original Internet standards it wasn't allowed to use network
    bits of all 0's or all 1's, so we used to have to substract 2 to
    get the number of networks. The `ip subnet-zero` command on a
    router overrides the limitation.
- `\31` subnets are supported on Cisco Routers for *point to point*
    links (which have no need for a network or broadcast address).
    It's useful if you need to maximise use of your address space.
    `/30` is more standard and commonly used. For the `CCNA exam`, use
    `/30` when a subnet to support 2 hosts is required, unless told to
    use `/31`.

## Trivia

- Early routing protocols only supported *Fixed Length Subnet Masking*
    (FLSF). You couldn't have have subnets with different size in the
    same network. All modern routing protocols support *Variable LSM*.
