<p align="center">
 Simply use a radix tree to blacklist ip addresses 
</p>
<!-- <p align="center">
   <a href="https://goreportcard.com/report/github.com/imthaghost/goclone"><img src="https://goreportcard.com/badge/github.com/imthaghost/goclone"></a>
   <a href="https://github.com/imthaghost/gitmoji-changelog">
    <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"alt="gitmoji-changelog">
  </a>
</p> -->
<br>



## Examples

```python
	from radix import radix

	# Create a new tree
	rtree = radix.Radix()

	# Adding a node returns a RadixNode object. You can create
	# arbitrary members in its 'data' dict to store your data
	rnode = rtree.add("10.0.0.0/8")
	rnode.data["blah"] = "whatever you want"

	# You can specify nodes as CIDR addresses, or networks with
	# separate mask lengths. The following three invocations are
	# identical:
	rnode = rtree.add("10.0.0.0/16")
	rnode = rtree.add("10.0.0.0", 16)
	rnode = rtree.add(network = "10.0.0.0", masklen = 16)

	# It is also possible to specify nodes using binary packed
	# addresses, such as those returned by the socket module
	# functions. In this case, the radix module will assume that
	# a four-byte address is an IPv4 address and a sixteen-byte
	# address is an IPv6 address. For example:
	binary_addr = inet_ntoa("172.18.22.0")
	rnode = rtree.add(packed = binary_addr, masklen = 23)

	# Exact search will only return prefixes you have entered
	# You can use all of the above ways to specify the address
	rnode = rtree.search_exact("10.0.0.0/8")
	# Get your data back out
	print rnode.data["blah"]
	# Use a packed address
	addr = socket.inet_ntoa("10.0.0.0")
	rnode = rtree.search_exact(packed = addr, masklen = 8)

	# Best-match search will return the longest matching prefix
	# that contains the search term (routing-style lookup)
	rnode = rtree.search_best("10.123.45.6")

	# Worst-search will return the shortest matching prefix
	# that contains the search term (inverse routing-style lookup)
	rnode = rtree.search_worst("10.123.45.6")

	# Covered search will return all prefixes inside the given
	# search term, as a list (including the search term itself,
	# if present in the tree)
	rnodes = rtree.search_covered("10.123.0.0/16")

	# There are a couple of implicit members of a RadixNode:
	print rnode.network	# -> "10.0.0.0"
	print rnode.prefix	# -> "10.0.0.0/8"
	print rnode.prefixlen	# -> 8
	print rnode.family	# -> socket.AF_INET
	print rnode.packed	# -> '\n\x00\x00\x00'

	# IPv6 prefixes are fully supported in the same tree
	rnode = rtree.add("2001:DB8::/3")
	rnode = rtree.add("::/0")

	# Use the nodes() method to return all RadixNodes created
	nodes = rtree.nodes()
	for rnode in nodes:
		print rnode.prefix

	# The prefixes() method will return all the prefixes (as a
	# list of strings) that have been entered
	prefixes = rtree.prefixes()

	# You can also directly iterate over the tree itself
	# this would save some memory if the tree is big
	# NB. Don't modify the tree (add or delete nodes) while
	# iterating otherwise you will abort the iteration and
	# receive a RuntimeWarning. Changing a node's data dict
	# is permitted.
	for rnode in rtree:
  		print rnode.prefix
```
## 📝 License

By contributing, you agree that your contributions will be licensed under its MIT License.

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.



