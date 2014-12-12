import os

def dostuff(f):
    
    output = []
    
    f = open(f,'r')
    print "opened file..."
    lines = [x for x in f]
    _l = [l.strip('\n') for l in lines]
    _l = [e for e in _l if e != ""]
    
    _date = _l[0].split(" - ")[1]
    setcounter = 0
    current_reps = 0
    current_lbs = 0
    current_exercise = ""
    notes = ""
    
    output.append( "{0},{1},{2},{3},{4},{5}".format('date','exercise','set','lbs','reps','notes'))
    for e in _l:
      if e[:2] == "**":
        current_exercise = e.strip('**').strip()
        setcounter = 0 #reset it for new exercise
      elif e[0] == "-":
          setcounter += 1
          [current_lbs, current_reps] = e.lstrip('- ').split(' x ')
          _temp = current_reps.split('[')
          if(len(_temp) == 2):
            [current_reps, notes] = current_reps.rstrip(']').split('[')
          else:
              notes = ""
              
          output.append( '"{0}","{1}",{2},{3},{4},"{5}"'.format(_date, current_exercise,setcounter,current_lbs.split('.0 lbs')[0],current_reps.rstrip(' reps'), notes))
    
    f.close()
    f = open('FitNotes_{0}'.format(_date),'w')
    for l in output:
        f.write(l+'\n')
    f.close()

dirname = 'WorkoutLog'
for root, dirs, files in os.walk(dirname):
    print "in the dir" 
    for f in files:
        print "doing stuff on file...{0}/{1}".format(dirname,f)
        dostuff("{0}/{1}".format(dirname,f))
        
