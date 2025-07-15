# 20CYS402 - Distributed Systems and Cloud Computing
![](https://img.shields.io/badge/Batch-22CYS-lightgreen) ![](https://img.shields.io/badge/UG-blue) ![](https://img.shields.io/badge/Subject-DSCC-blue) <br/>

## Lab 2: Interplanetary File System (IPFS) 
![](https://img.shields.io/badge/15_Jul-blue) ![](https://img.shields.io/badge/16_Jul-darkred)

### IPFS

### Tools Exploration
- [IPFS Client (kubo-ipfs)](https://docs.ipfs.tech/install/command-line/#next-steps)
- [IPFS Companion (Browser Plugin)](https://docs.ipfs.tech/install/ipfs-companion/)
- [IPFS Desktop](https://docs.ipfs.tech/install/ipfs-desktop/)

### Understanding
- ipfs commands (add, get, cat)
- ipfs chuncking method and dag visualization
- ipfs config file
- [CID inspector](https://cid.ipfs.tech/)
- [IPLD Explorer](https://explore.ipld.io/)
- [Multiformats](https://multiformats.io/)

### IPFS Commands

- Initialize IPFS Node 

```
ipfs init
```

- Get the PEER ID

```
ipfs id
```

- Add a file to IPFS (this will return the Content hash commonly referred as CID - Content Identifier)

```
ipfs add <filename>
```

- Add a folder recursively

```
ipfs add -r <folder>
```

- Get the content of the file using CID 

```
ipfs cat <CID>
```

- Download a file using CID

```
ipfs get <CID>
```

- Pin a file to IPFS (avoid from Garbage Collection)

```
ipfs pin add <CID>
```

- Garbage Collect (this will remove all unpinned items)
  
```
ipfs repo gc
```

- Run a daemon

```
ipfs daemon
```

### Setup Private IPFS 

- Generate Swarm Key and save it as ```swarm.key```

  ```
  $bytes = New-Object byte[] 32
  [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
  $hex = -join ($bytes | ForEach-Object { $_.ToString("x2") })
  $hex
  ```

- Copy the ```swarm.key``` to ```.ipfs``` folder
  
- Remove all the bootstrap nodes

  ```
  ipfs bootstrap rm --all
  ```
- Add only nodes that are to be part of the network

  ```
  ipfs bootstrap add /ip4/<IP_ADDRESS>/tcp/4001/p2p/<PEER_ID>
  ```
- Run the Daemon
