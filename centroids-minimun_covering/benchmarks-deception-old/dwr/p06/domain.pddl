(define (domain dwr)
 (:requirements :strips :typing :negative-preconditions)
 (:types 
  location
  pile
  robot
  crane
  container)

 (:predicates
   (adjacent ?l1  ?l2 - location)
   (attached ?p - pile ?l - location)
   (belong ?k - crane ?l - location)
   (at ?r - robot ?l - location)
   (occupied ?l - location)
   (loaded ?r - robot ?c - container)
   (unloaded ?r - robot)
   (holding ?k - crane ?c - container)
   (empty ?k - crane)
   (in ?c - container ?p - pile)
   (top ?c - container ?p - pile)
   (on ?k1 - container ?k2 - container)
)

(:action move                                
  :parameters (?r - robot ?from - location ?to - location)
  :precondition (and (adjacent ?from ?to)
                  (at ?r ?from))
  :effect (and 
    (at ?r ?to)
    (not (occupied ?from))
    (occupied ?to)
    (not (at ?r ?from)) 
  )
)

(:action load
  :parameters (?k - crane ?c - container ?r - robot ?l - location)
  :precondition (and (at ?r ?l) (belong ?k ?l)
                  (holding ?k ?c) (unloaded ?r))
  :effect (and
    (loaded ?r ?c)
    (not (unloaded ?r))
    (empty ?k)
    (not (holding ?k ?c))
  )
)

(:action unload
  :parameters (?k - crane ?c - container ?r - robot ?l - location)
  :precondition (and (belong ?k ?l) (at ?r ?l)
                  (loaded ?r ?c) (empty ?k))
  :effect (and
    (unloaded ?r)
    (holding ?k ?c)
    (not (loaded ?r ?c))
    (not (empty ?k))
  )
)

(:action take
  :parameters (?k - crane ?c - container ?p - pile ?else - container ?l - location)
  :precondition (and (belong ?k ?l)(attached ?p ?l)
                   (empty ?k) (in ?c ?p) 
                   (top ?c ?p) (on ?c ?else))
  :effect (and
    (holding ?k ?c)
    (top ?else ?p)
    (not (in ?c ?p))
    (not (top ?c ?p))
    (not (on ?c ?else))
    (not (empty ?k))
  )
)

(:action put                                 
  :parameters (?k - crane ?c - container ?p - pile ?else - container ?l - location)
  :precondition (and (belong ?k ?l) (attached ?p ?l)
                  (holding ?k ?c) (top ?else ?p))
  :effect (and
    (in ?c ?p)
    (top ?c ?p)
    (on ?c ?else)
    (not (top ?else ?p))
    (not (holding ?k ?c))
    (empty ?k)
  )
)
)