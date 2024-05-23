Demonstrate the phylogenetic placement pipeline of Kssdtree using an assembled prokaryotic genome, including a multi-step implementation and a one-step implementation.

# Multi-step implementation
```
import kssdtree

# step1、sketching gtdbr214 (pre-sketching and hosting server) and an assembled prokaryotic genome - GCF_001228905.1 (PROK1) with L3K9.shuf
kssdtree.sketch(shuf_file='L3K9.shuf', genome_files='gtdbr214', output='gtdbr214_sketch', set_opt=True)
kssdtree.sketch(shuf_file='L3K9.shuf', genome_files='PROK1', output='PROK1_sketch', set_opt=True)

# step2、retrieving 30 closest sketches (taxonomies) from gtdbr214_sketch (gtdbr214_taxonomy.txt), calculating and creating distance matrix in phylip format required by NJ, and constructing tree with NJ, it will create output.newick and output_accession_taxonomy.txt in PROK31 folder.
kssdtree.retrieve(ref_sketch='gtdbr214_sketch', qry_sketch='PROK1_sketch', output='PROK31', N=30, method='nj')

# step3、visualizing tree 
kssdtree.visualize(newick='./PROK31/output.newick', taxonomy='./PROK31/output_accession_taxonomy', mode='r')
```

# One-step implementation (Recommendation)
```
import kssdtree

kssdtree.quick(shuf_file='L3K9.shuf', genome_files='PROK1', output='PROK31', reference='gtdbr214_sketch', method='nj', mode='r', N=30)
```

Output:
![3.png](http://www.metakssdcoabundance.link/kssdtree/pngs/3.png)
