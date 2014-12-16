#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def dostuff(f):
    
    output = []
    lines = [x for x in f]
    _l = [l.strip('\n') for l in lines]
    _l = [e for e in _l if e != '']

    _date = _l[0].split(' - ')[1]
    setcounter = 0
    current_reps = 0
    current_lbs = 0
    current_exercise = ''
    notes = ''

    for e in _l:
        if e[:2] == '**':
            current_exercise = e.strip('**').strip()
            setcounter = 0  # reset it for new exercise
        elif e[0] == '-':
            setcounter += 1
            try:
                [current_lbs, current_reps] = e.lstrip('- ').split(' x ')
            except ValueError, e:
                [current_lbs, current_reps] = ['-2','-2']
           
            print current_reps.split('rep')[0]
            print current_reps.split('rep')[1].lstrip('s')
            #have to handle 'rep' instead of 'reps' case
            [current_reps, notes] = [current_reps.split('rep')[0],current_reps.split('rep')[1].lstrip('s')]
            output.append('"{0}","{1}",{2},{3},{4},"{5}"'.format(
                _date,
                current_exercise,
                setcounter,
                current_lbs.split('.0 lbs')[0],
                current_reps,
                notes,
                ))

    f.close()
    return output


dirname = 'WorkoutLog'
output = []
output.append('{0},{1},{2},{3},{4},{5}'.format(
    'date',
    'exercise',
    'set',
    'lbs',
    'reps',
    'notes',
    ))

for (root, dirs, files) in os.walk(dirname):
    print 'in the dir {0}'.format(dirname)
    for f in files:
        print 'opened file...{0}'.format(f)
        f = open('{0}/{1}'.format(dirname, f), 'r')
        print 'doing stuff on file...{0}/{1}'.format(dirname, f)
        output.extend(dostuff(f))
        f.close()

f = open('FitNotes.csv', 'w')
for l in output:
    f.write(l + '\n')

			
