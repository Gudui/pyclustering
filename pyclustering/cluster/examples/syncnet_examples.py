"""!

@brief Examples of usage and demonstration of abilities of Sync algorithm in cluster analysis.

@authors Andrei Novikov (pyclustering@yandex.ru)
@date 2014-2016
@copyright GNU Public License

@cond GNU_PUBLIC_LICENSE
    PyClustering is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    PyClustering is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
@endcond

"""

from pyclustering.cluster.syncnet import syncnet;
from pyclustering.nnet.sync import sync_visualizer;

from pyclustering.nnet import solve_type;

from pyclustering.samples.definitions import SIMPLE_SAMPLES;
from pyclustering.samples.definitions import FCPS_SAMPLES;

from pyclustering.utils import draw_clusters;
from pyclustering.utils import read_sample;
from pyclustering.utils import timedcall;


def template_clustering(file, radius, order, show_dyn = False, show_conn = False, show_clusters = True, ena_conn_weight = False, ccore_flag = True):
    sample = read_sample(file);
    network = syncnet(sample, radius, enable_conn_weight = ena_conn_weight, ccore = ccore_flag);
    
    (ticks, analyser) = timedcall(network.process, order, solve_type.FAST, show_dyn);
    print("Sample: ", file, "\t\tExecution time: ", ticks, "\n");
    
    if (show_dyn == True):
        sync_visualizer.show_output_dynamic(analyser);
        sync_visualizer.animate_output_dynamic(analyser);
    
    if ( (show_conn == True) and (ccore_flag == False) ):
        network.show_network();
    
    if (show_clusters == True):
        clusters = analyser.allocate_clusters();
        draw_clusters(sample, clusters);
    
    
def cluster_simple1():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, show_dyn = True, show_conn = True);
    
def cluster_simple2():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, show_dyn = True, show_conn = True);
    
def cluster_simple3():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, 0.999, show_dyn = True, show_conn = True);

def cluster_simple4():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 1, 0.999, show_dyn = True, show_conn = True);
    
def cluster_simple5():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 1, 0.999, show_dyn = True, show_conn = True);

def cluster_elongate():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_ELONGATE, 0.5, 0.999, show_dyn = True, show_conn = True);

def cluster_lsun():
    template_clustering(FCPS_SAMPLES.SAMPLE_LSUN, 0.3, 0.999, show_dyn = True, show_conn = True);

def cluster_hepta():
    template_clustering(FCPS_SAMPLES.SAMPLE_HEPTA, 1, 0.999, show_dyn = True, show_conn = True);
    
def cluster_chainlink():
    template_clustering(FCPS_SAMPLES.SAMPLE_CHAINLINK, 0.5, 0.999, show_dyn = True, show_conn = True);

def cluster_two_diamonds():
    template_clustering(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, 0.03, 0.999, show_dyn = False, show_conn = False);  

def cluster_atom():
    template_clustering(FCPS_SAMPLES.SAMPLE_ATOM, 20, 0.999, show_dyn = False, show_conn = False); 
    
def cluster_wing_nut():
    template_clustering(FCPS_SAMPLES.SAMPLE_WING_NUT, 0.08, 0.999, show_dyn = False, show_conn = False); 

def experiment_execution_time(show_dyn = False, ccore = False):
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 1, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 1, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(SIMPLE_SAMPLES.SAMPLE_ELONGATE, 0.5, 0.999, show_dyn, False, True, False, ccore);
    
    template_clustering(FCPS_SAMPLES.SAMPLE_LSUN, 0.3, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(FCPS_SAMPLES.SAMPLE_TARGET, 0.4, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, 0.03, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(FCPS_SAMPLES.SAMPLE_WING_NUT, 0.08, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(FCPS_SAMPLES.SAMPLE_CHAINLINK, 0.5, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(FCPS_SAMPLES.SAMPLE_HEPTA, 1, 0.999, show_dyn, False, True, False, ccore);
    template_clustering(FCPS_SAMPLES.SAMPLE_TETRA, 0.3, 0.999, show_dyn, False, True, False, ccore);

def cluster_simple1_conn_weight():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, 0.999, show_dyn = True, show_conn = True, ena_conn_weight = True); 
    
def cluster_simple2_conn_weight():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 2, 0.999, show_dyn = True, show_conn = True, ena_conn_weight = True);   

def cluster_simple3_conn_weight():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 2, 0.999, show_dyn = True, show_conn = True, ena_conn_weight = True);

def cluster_simple4_conn_weight():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 10, 0.999, show_dyn = True, show_conn = True, ena_conn_weight = True);

def cluster_simple5_conn_weight():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 10, 0.999, show_dyn = True, show_conn = True, ena_conn_weight = True);


cluster_simple1();
cluster_simple2();
cluster_simple3();
cluster_simple4();
cluster_simple5();
cluster_elongate();
cluster_lsun();
cluster_hepta();
cluster_chainlink();
cluster_two_diamonds();
cluster_atom();
cluster_wing_nut();
      
cluster_simple1_conn_weight();
cluster_simple2_conn_weight();
cluster_simple3_conn_weight();
cluster_simple4_conn_weight();
cluster_simple5_conn_weight();
 
experiment_execution_time(False, False);
experiment_execution_time(True, True);