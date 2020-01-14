# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from qiskit import transpiler
from qiskit.test import mock

backend = mock.FakeYorktown()
basis = backend.configuration().basis_gates
coupling = transpiler.CouplingMap(backend.configuration().coupling_map)
props = backend.properties()

config = transpiler.transpile_config.TranspileConfig(validate=False,
                                                     basis_gates=basis,
                                                     coupling_map=coupling,
                                                     initial_layout=None,
                                                     seed_transpiler=None,
                                                     backend_properties=props,
                                                     optimization_level=0)

pm0 = transpiler.preset_passmanagers.level_0_pass_manager(config)
pm0.draw(filename='preset_level_0.png')

config = transpiler.transpile_config.TranspileConfig(validate=False,
                                                     basis_gates=basis,
                                                     coupling_map=coupling,
                                                     initial_layout=None,
                                                     seed_transpiler=None,
                                                     backend_properties=props,
                                                     optimization_level=1)

pm1 = transpiler.preset_passmanagers.level_1_pass_manager(config)
pm1.draw(filename='preset_level_1.png')

config = transpiler.transpile_config.TranspileConfig(validate=False,
                                                     basis_gates=basis,
                                                     coupling_map=coupling,
                                                     initial_layout=None,
                                                     seed_transpiler=None,
                                                     backend_properties=props,
                                                     optimization_level=2)

pm2 = transpiler.preset_passmanagers.level_2_pass_manager(config)
pm2.draw(filename='preset_level_2.png')

config = transpiler.transpile_config.TranspileConfig(validate=False,
                                                     basis_gates=basis,
                                                     coupling_map=coupling,
                                                     initial_layout=None,
                                                     seed_transpiler=None,
                                                     backend_properties=props,
                                                     optimization_level=3)

pm3 = transpiler.preset_passmanagers.level_3_pass_manager(config)
pm3.draw(filename='preset_level_3.png')
