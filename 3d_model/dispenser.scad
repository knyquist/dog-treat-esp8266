$fs=0.5;
$fa = 0.5;

module hollow_cylinder() {
    difference() {
        translate([0, 0, -30]) {
            r1 = 30;
            h1 = 60;
            cylinder(d = 2 * r1, h = h1);
        }
        translate([0, 0, -27.5]) {
            r2 = 27.5;
            h2 = 55;
            cylinder(d = 2 * r2, h =  h2);
        }
    }
}

module rounded_cube(L1, L2) {
    color("red") {
        cyl_r = L1 / 3;
        cube_len1 = L1 - 2 * cyl_r;
        cube_len2 = L2 - 2 * cyl_r;
        translate([cyl_r, cyl_r, 0]) {
            minkowski() {
                cube([cube_len1, cube_len2, 10]);
                cylinder(r = cyl_r, h = 1);
            }
        }
    }
}

module top_hole() {
    translate([7.5, -15, 25])
    rounded_cube(L1 = 15, L2 = 30);
}

module bottom_hole() {
    translate([-7.5 - 15, -15, -35])
    rounded_cube(L1 = 15, L2 = 30);
}

//bottom_hole();

module treat_reservoir() {
    difference() {
        hollow_cylinder();
        translate([0, 0, -50]) {
            cylinder(d = 7, h = 100);
        }
    }
}

difference() {
    treat_reservoir();
    top_hole();
    bottom_hole();
}
