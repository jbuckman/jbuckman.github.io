import ipdb
import numpy as np
from bokeh.plotting import figure, output_file, save

p = figure(width=700, height=500)
output_file(filename="stpetersburg.html", title="Doubling game")

parallel = 10_000_000
steps = 2000
rounds_played = 0.
sum_of_payoffs = 0.
record_rounds = []
record_payoffs = []
for i in range(steps):
  wins = np.sum(np.cumsum(np.random.randint(0,2,[parallel, 100]), -1) == 0., -1)
  assert not (wins == 100).any()
  rounds_played += parallel
  sum_of_payoffs += np.sum(2 ** (wins+1))
  record_rounds.append(rounds_played)
  record_payoffs.append(sum_of_payoffs)
  print(f"{(i+1)/steps:.2%} {sum_of_payoffs/rounds_played:4.4} {np.log2(rounds_played):4.4}")

x = np.array(record_rounds)
y = np.array(record_payoffs)
p.line(x, y / x, legend_label="Empirical mean payout", color='black', alpha=.8)
p.line(x, np.log2(x), legend_label="log2(n)", color='blue')
save(p)