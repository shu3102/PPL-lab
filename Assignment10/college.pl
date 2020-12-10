teaches_subject(t1,math).

teaches_subject(t2,math).

teaches_subject(t3,dsa).

teaches_subject(t4,ppl).

teaches_subject(t5,dld).

teaches_subject(t6,dtl).



has_subject(math_dept,math).

has_subject(comp_dept,dsa).

has_subject(comp_dept,ppl).

has_subject(comp_dept,dtl).





has_student(comp_dept,s1).

has_student(comp_dept,s2).





has_faculty(D,F) :- teaches_subject(F,S) , has_subject(D,S).

studies_subject(ST,SB) :- has_student(D,ST) , has_subject(D,SB).

studies_under(S,F) :- has_subject(D,SB) , has_student(D,S) , teaches_subject(F,SB).
