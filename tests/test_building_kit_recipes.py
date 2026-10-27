"""Geometric promotion must distinguish a real aperture from a filled wall."""
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from building_kit_recipes import covered,offset,aperture_clear
from building_builder import compile_layout,kit


class RecipeTests(unittest.TestCase):
    def test_ray_projection_separates_frame_from_aperture(self):
        def rectangle(x0,z0,x1,z1):
            return [[(x0,z0),(x1,z0),(x1,z1)],[(x0,z0),(x1,z1),(x0,z1)]]
        frame=rectangle(-3,0,-2.25,4)+rectangle(-.75,0,0,4)+rectangle(-2.25,2.4,-.75,4)
        self.assertFalse(covered(frame,-1.5,1.2))
        self.assertTrue(aperture_clear(frame))
        self.assertTrue(covered(frame,-2.6,1.2))
        self.assertTrue(covered(frame,-1.5,3))
        filled=frame+rectangle(-2.25,0,-.75,2.4)
        self.assertTrue(covered(filled,-1.5,1.2))
        # A narrow obstruction between sample rays must still reject the frame.
        self.assertFalse(aperture_clear(frame+rectangle(-1.63,1.33,-1.61,1.35)))

    def test_offset_normalises_measured_pivot_without_scaling(self):
        self.assertEqual(offset({"geometry":{"min":[0,-.2,1],"max":[3,0,5]}}),[-3,.2,-1])

    def test_piece_offset_rotates_with_its_wall_and_world_anchor(self):
        layout=json.loads((ROOT/"projects/experiments/building-lab/buildings/workshop.building.json").read_bytes())
        original=compile_layout(layout)
        recipe=copy.deepcopy(kit(layout["kit"]));recipe["pieces"]["wall"]["offset"]=[.2,.1,.05]
        with patch("building_builder.kit",return_value=recipe): changed=compile_layout(layout)
        before=next(i for i in original["instances"] if i["role"]=="wall" and i["yaw"]==90)
        after=next(i for i in changed["instances"] if i["id"]==before["id"])
        for a,b in zip(after["position"],[before["position"][0]-.1,before["position"][1]+.2,before["position"][2]+.05]):
            self.assertAlmostEqual(a,b)
        self.assertEqual(original["solids"],changed["solids"])


if __name__=="__main__":unittest.main()
