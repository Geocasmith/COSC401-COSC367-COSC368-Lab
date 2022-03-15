solution(V1,V2,V3,H1,H2,H3):-
word(V1, _,H1V1,_,H2V1,_,H3V1,_),
word(V2, _,H1V2,_,H2V2,_,H3V2,_),
word(V3, _,H1V3,_,H2V3,_,H3V3,_),
word(H1, _,H1V1,_,H1V2,_,H1V3,_),
word(H2, _,H2V1,_,H2V2,_,H2V3,_),
word(H3, _,H3V1,_,H3V2,_,H3V3,_).


word(curious,c,u,r,i,o,u,s).
word(bobsled,b,o,b,s,l,e,d).
word(quizzes,q,u,i,z,z,e,s).
word(realize,r,e,a,l,i,z,e).
word(aimless,a,i,m,l,e,s,s).
word(jukebox,j,u,k,e,b,o,x).

test_answer :-
    findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
    sort(L,S),
    foreach(member(X,S), (write(X), nl)).

test_answer :- write('Wrong answer!'),
    halt.