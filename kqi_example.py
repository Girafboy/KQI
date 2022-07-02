import json
import datetime
import pandas as pd

import util.kqi as kqi

if __name__ == '__main__':
    # Load example data
    data = pd.read_csv('data_example.csv', index_col=0, encoding='utf-8_sig')

    # Create graph
    G = kqi.DiGraph()

    # Add nodes and edges, parameters in order (new nodes added, list of parent nodes, new nodes' created time)
    for id in data.index:
        G.add_node(id, json.loads(data.loc[id, 'referenceids']), datetime.date.fromisoformat(data.loc[id, 'date']))

    # De-cycling to form DAG
    G.remove_cycles()
    # Set the current date
    G.set_today(datetime.date.today())
    # Set the attenuation coefficient (1 that is, no attenuation, 0 that is, the maximum attenuation rate)
    G.set_decay(1)

    # Calculate KQI
    data['kqi'] = [G.kqi(k) for k in data.index]

    # Sort and output files
    data.sort_values('kqi', ascending=False).to_csv('result_example.csv', encoding='utf-8_sig')