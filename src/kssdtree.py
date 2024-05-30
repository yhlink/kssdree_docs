def shuffle(k=None, s=None, l=None, o=None):
    """
    Generating a .shuf file.

    Args:
        k (int): Half-length of k-mer. k=x means using k-mer of length 2x.
        s (int): Half-length of k-mer substring. s=x means the whole space is the collection of all 2x-mers. Make sure l < s < k. Default is -s 6, usually there's no need to change this setting.
        l (int): The level of dimensionality-reduction. l=x means the expected rate of dimensionality-reduction is 16^x.
        o (str): Output filename of the .shuf file.

    Returns:
        bool: True or False

    Example:
        >>> kssdtree.shuffle(k=10, s=6, l=3, o='L3K10.shuf')
        True
    """
    return True


def sketch(shuf_file=None, genome_files=None, output=None, set_opt=None):
    """
    Sketching genomes and generating sketch result files.

    Args:
        shuf_file (str): Path to the .shuf file. Kssdtree provides multiple .shuf files ('L3K9.shuf', 'L3K10.shuf', etc.) as input for genome sketching. Default is 'L3K10.shuf'.
        genome_files (str): Path to the folder containing genome files. Kssdtree supports input of genome files in both fasta and fastq formats.
        output (str): Output folder path for sketch result files of genome files.
        set_opt (bool): Perform set operations (subtract and retrieve) if needed. Default is False. To perform set operations, set set_opt=True.

    Returns:
        bool: True or False

    Example:
        >>> kssdtree.sketch(shuf_file='L3K10.shuf', genome_files='ES29', output='ES29_sketch')
        True
        >>> kssdtree.sketch(shuf_file='../shuf_file/L3K10.shuf', genome_files='../data/ES29', output='ES29_sketch')
        True
        >>> kssdtree.sketch(shuf_file='L3K10.shuf', genome_files='hg38.fa.gz', output='Ref_sketch', set_opt=True)
        True
        >>> kssdtree.sketch(shuf_file='L3K10.shuf', genome_files='HG43', output='HG43_sketch', set_opt=True)
        True
        >>> kssdtree.sketch(shuf_file='L3K9.shuf', genome_files='gtdbr214', output='gtdbr214_sketch', set_opt=True)
        True
        >>> kssdtree.sketch(shuf_file='L3K9.shuf', genome_files='PROK1', output='PROK1_sketch', set_opt=True)
        True
    """
    return True


def dist(ref_sketch=None, qry_sketch=None, output=None, flag=None):
    """

        Calculating pairwise distances between reference and query, then generating distance matrix in phylip format.

        Args:
            ref_sketch (str): Path to the folder containing sketch result files for reference genomes.
            qry_sketch (str): Path to the folder containing sketch result files for query genomes.
            output (str): Filename for the output distance matrix in phylip format.
            flag (int): Specifies the format to generate the distance matrix, where 0 is for NJ algorithm (with zeros on the diagonal), and 1 is for DNJ algorithm (without the diagonal elements).

        Returns:
            bool: True or False

        Example:
            >>> kssdtree.dist(ref_sketch='ES29_sketch', qry_sketch='ES29_sketch', output='ES29.phylip', flag=0)
            True
            >>> kssdtree.dist(ref_sketch='ES29_sketch', qry_sketch='ES29_sketch', output='ES29.phylip', flag=1)
            True
            >>> kssdtree.dist(ref_sketch='HG43_sub_sketch', qry_sketch='HG43_sub_sketch', output='HG43.phylip', flag=0)
            True
            
    """
    return True


def retrieve(ref_sketch=None, qry_sketch=None, output=None, N=None, method=None):
    """
        Retrieving the X*N closest sketches (regard as the backbone or reference tree) from gtdbr214_sketch, where X is genome number containing qry_sketch. Calculating distance matrix and constructing tree. Creating output.newick and output_accession_taxonomy.txt in the output folder.

        Args:
            ref_sketch (str): Path to the folder containing sketch result files of reference genomes.
            qry_sketch (str): Path to the folder containing sketch result files of query genomes.
            output (str): Path to the output folder for the retrieved sketch result files.
            N (int): Maximum number of closest reference genomes to retrieve.
            method (str): Method for constructing the tree, either 'nj' (NJ) or 'dnj' (DNJ). Defaults to 'nj'.


        Returns:
            bool: True or False

        Example:
            >>> kssdtree.retrieve(ref_sketch='gtdbr214_sketch', qry_sketch='PROK1_sketch', output='PROK31', N=30, method='nj') 
            True
    """
    return True


def build(phylip=None, output=None, method=None):
    """
        Constructing tree with NJ or DNJ method and generating it in newick format.

        Args:
            phylip (str): Path to the distance matrix file in phylip format.
            output (str): Filename for the output tree in newick format.
            method (str): Method for constructing the tree, either 'nj' (NJ) or 'dnj' (DNJ). Defaults to 'nj'.

        Returns:
            bool: True or False

        Example:
            >>> kssdtree.build(phylip='ES29.phylip', output='ES29.newick', method='nj')
            True
            >>> kssdtree.build(phylip='ES29.phylip', output='ES29.newick', method='dnj')
            True
          
    """
    return True


def visualize(newick=None, taxonomy=None, mode=None):
    """
        Visualizing tree with the ETE3 toolkit.

        Args:
            newick (str): Path to the tree file in newick format.
            taxonomy (str): Path to the taxonomy information file in txt format, which records the name (accession) of genomes and their taxonomy. Default is None.
            mode (str): Visualization mode, either 'r' (rectangle) or 'c' (circle). Default is 'r'.

        Returns:
            bool: True or False

        Example:
            >>> kssdtree.visualize(newick='ES29.newick', mode='r')
            True
            >>> kssdtree.visualize(newick='ES29.newick', mode='c')
            True
            >>> kssdtree.visualize(newick='HG43.newick', taxonomy='HG43.txt', mode='r')
            True
            >>> kssdtree.visualize(newick='./PROK31/output.newick', taxonomy='./PROK31/output_accession_taxonomy', mode='r')
            True
            
    """
    return True


def subtract(ref_sketch=None, genome_sketch=None, output=None):
    """
        Subtracting the reference sketches from the genome sketches and creating the remainder sketch files.

        Args:
            ref_sketch (str): Path to the folder containing sketch result files of reference genomes.
            genome_sketch (str): Path to the folder containing sketch result files of genomes.
            output (str): Path to the output folder for the remainder sketch result files.

        Returns:
            bool: True or False

        Example:
            >>> kssdtree.subtract(ref_sketch='Ref_sketch', genome_sketch='HG43_sketch', output='HG43_sub_sketch')
            True
    """
    return True


def quick(shuf_file=None, genome_files=None, output=None, reference=None, taxonomy=None, method=None, mode=None, N=None):
    """
        Simplifying the pipeline and eliminating the necessity of organizing many intermediate files.

        Args:
            shuf_file (str): Path to the .shuf file. Kssdtree provides multiple .shuf files ('L3K9.shuf', 'L3K10.shuf', etc.) as input for genome sketching. Default is 'L3K10.shuf'. For phylogenetic placement, 'L3K9.shuf' file must be used.
            genome_files (str): Path to the folder containing genome files. Kssdtree supports input of genome files in both fasta and fastq formats.
            output (str): For routine and reference subtraction pipelines, the output is a .newick format file. For phylogenetic placement pipeline, the output is a folder, including output.newick and output_accession_taxonomy.txt.
            reference (str): If None, performs the routine workflow. If set to the reference genome file or folder path, performs the reference subtraction workflow. For phylogenetic placement, set to 'gtdbr214_sketch'.
            taxonomy (str): Filename for the taxonomy information in txt format, which records the name (accession) of genomes and their taxonomy. Default is None.
            method (str): Method for constructing the tree, either 'nj' (NJ) or 'dnj' (DNJ). Default is 'nj'.
            mode (str): Visualization mode, either 'r' (rectangle) or 'c' (circle). Default is 'r'.
            N (int): Maximum number of nearest reference genomes. Default is 0 for routine and reference subtraction pipelines. For phylogenetic placement pipeline, set N > 0.

        Returns:
            bool: True or False

        Example:
            >>> kssdtree.quick(shuf_file='L3K10.shuf', genome_files='ES29', output='ES29.newick',  method='nj', mode='r')
            True
            >>> kssdtree.quick(shuf_file='L3K10.shuf', genome_files='HG43', output='HG43.newick', reference='hg38.fa.gz', taxonomy='HG43.txt', method='nj', mode='r')
            True
            >>> kssdtree.quick(shuf_file='L3K9.shuf', genome_files='PROK1', output='PROK31', reference='gtdbr214_sketch', method='nj', mode='r', N=30)
            True
    """
    return True