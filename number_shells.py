import networkx as nx 

p=0.1
while (p<=1):
	
	name='num_shells'+str(p)
	f = open(name,'w')
	for i in range (10,1000):
		G=nx.erdos_renyi_graph(i,0.1)
		c=nx.core_number(G)
		s=[]
		for each in c:
			s.append(c[each])
	
		print 'prob=',p,'num=',i
		f.write(str(max(s))+'\n')
	f.close()
