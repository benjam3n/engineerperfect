# Maintaining service while equipment is repaired

Better dispatch cannot sustain this service with one worker. Concurrent repair makes a sustainable operation possible from every initial wear state except the state in which both stations already need repair. This changes the recommendation from selecting a cleverer schedule to supplying the missing simultaneous contribution; persuading everybody to accept the original schedule would leave its limit unchanged.

A constructed service has two stations, A and B. Each station can complete two jobs after a repair. Its wear state is 0, 1, or 2; state 2 cannot serve another job until repaired. Exactly one job must be completed in every period. Serving one job takes one worker for the whole period and increases the active station's wear by one. Repair takes another worker for the whole period and resets the idle station's wear to 0. A station cannot serve and be repaired in the same period.

No unplanned faults, partial repairs, worker absence, or job buffering are admitted. The model can describe a stipulated service arrangement without asserting measured properties of real equipment or people.

## One worker cannot sustain the service

Every period's sole worker must serve the arriving job. Therefore no repair can occur without missing that period's requirement. Starting at wear (0,0), total remaining service capacity is four jobs. Every possible dispatch policy consumes one of them each period. The fifth period must fail.

The exact invariant-set computation removes (2,2) first, then states with one remaining service, then two, then three, and finally (0,0). No initial wear state supports continuous service forever with one worker.

Adding identical stations gives more startup capacity but does not repair the long-run labor deficit. If s services and r repairs occur in n periods with one worker, then s + r ≤ n and s ≤ 2r + 4 for the original two stations. Combining them gives 3s ≤ 2n + 4. The asymptotic service rate cannot exceed 2/3 jobs per period even when missed immediate deadlines are relaxed into a throughput measure.

## Two concurrent workers supply a sustainable operation

If at least one station is usable, serve on a usable station and repair the other concurrently. After the period, the repaired station has wear 0 and can serve next. The station just used has wear at most 2. Repeating this rule ensures that a usable station always exists.

Starting at (0,0), one simple repeating sequence is

| Starting wear | Work during the period | Ending wear |
|---|---|---|
| (0,0) | Serve A; repair B | (1,0) |
| (1,0) | Serve B; repair A | (0,1) |
| (0,1) | Serve A; repair B | (1,0) |

Every state except (2,2) supports some preserving policy. From (2,2), both stations require repair and neither can meet the current service demand, so uninterrupted service is impossible from that initial condition. A startup repair period could create an admissible initial state, but that would require permitting the startup interruption.

The software computes all preserving actions. Its selected policy sometimes postpones repair until necessary; the simpler alternating policy above uses more restoration than needed but establishes the same existence result. The repository does not label it labor-cost optimal.

## The support capacity is part of the promised service

The first arrangement has enough immediate service labor, working equipment, and a known repair procedure. Those facts still fail to supply repair at the required time. The second arrangement supplies that missing concurrency.

An equivalent gap can occur when a maintained collection depends on editing time unavailable during active use, or when a team knows how to recover but nobody can recover it without abandoning the required service. Those transfers require their own actual durations and dependencies; this example establishes the logical shape and exact stipulated result.

Redundancy alone does not establish maintenance capacity, and maintenance knowledge does not establish maintenance availability. The actual sustainable unit is the service together with the resources that restore it.

[Finite model](../tools/run_examples.py) · [All nine-state results](../evidence/computed-results.json).
