Demonstrate the phylogenetic placement pipeline of Kssdtree using an assembled prokaryotic genome, including a multi-step implementation and a one-step implementation.

# Multi-step implementation
```
import kssdtree

# step1、sketching 29 E.coli/Shigella strains (ES29) with k-mer substring space shuffled file (L3K10.shuf)
kssdtree.sketch(shuf_file='L3K10.shuf', genome_files='ES29', output='ES29_sketch')

# step2、calculating and creating distance matrix in phylip format required by NJ
kssdtree.dist(ref_sketch='ES29_sketch', qry_sketch='ES29_sketch', output='ES29.phylip', flag=0)
# step2、calculating and creating distance matrix in phylip format required by DNJ (no diagonal elements)
kssdtree.dist(ref_sketch='ES29_sketch', qry_sketch='ES29_sketch', output='ES29.phylip', flag=1)

# step3、constructing tree with NJ
kssdtree.build(phylip='ES29.phylip', output='ES29.newick', method='nj')
# step3、constructing tree with DNJ
kssdtree.build(phylip='ES29.phylip', output='ES29.newick', method='dnj')

# step4、visualizing tree in rectangle mode
kssdtree.visualize(newick='ES29.newick', mode='r')
# step4、visualizing tree in circle mode
kssdtree.visualize(newick='ES29.newick', mode='c')
```

# One-step implementation (Recommendation)
```
import kssdtree

kssdtree.quick(shuf_file='L3K9.shuf', genome_files='PROK1', output='PROK31', reference='gtdbr214_sketch', method='nj', mode='r', N=30)
```