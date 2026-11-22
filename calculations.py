"""
BioFrame - Calculation Framework (74 kg Light Platform)
Parametric physics model for 4-stage segmented joint articulation, Capstan tendon friction,
0-Watt dual-opposing magnetic wedge locks, and lightweight structural material limits.
"""

import math


def calculate_segmented_joint_capstan_efficiency(
    total_bend_angle_deg=140.0,
    num_segments=4,
    friction_coeff_ptfe=0.04,
):
    """
    Calculates Capstan friction efficiency across a 4-stage segmented joint.
    Dividing a 140-degree bend into 4 sequential 35-degree segments reduces
    localized tendon stress and prevents bend-radius fatigue.
    
    Formula: T_out / T_in = e^(-mu * theta)
    """
    if num_segments <= 0 or total_bend_angle_deg < 0:
        return (0.0, 0.0)

    angle_per_segment_deg = total_bend_angle_deg / num_segments
    total_angle_rad = math.radians(total_bend_angle_deg)

    # Overall tendon transmission efficiency across all 4 segmented PTFE links
    transmission_efficiency = math.exp(-friction_coeff_ptfe * total_angle_rad)

    return (round(angle_per_segment_deg, 1), round(transmission_efficiency * 100, 2))


def calculate_wedge_lock_holding_capacity(
    total_limb_load_kn=2.8,
    parallel_locks=2,
    wedge_taper_angle_deg=6.0,
    inner_friction_coeff=0.45,
    outer_ptfe_friction=0.04,
):
    """
    Models the 0-Watt self-locking threshold and load distribution for dual-opposing
    magnetic wedge lock pairs in the 74 kg humanoid frame.
    
    Self-locking condition: tan(alpha) < (mu_inner - mu_outer) / (1 + mu_inner * mu_outer)
    """
    if total_limb_load_kn <= 0 or parallel_locks <= 0:
        return {"status": "INVALID_INPUT"}

    load_per_lock_kn = total_limb_load_kn / parallel_locks
    alpha_rad = math.radians(wedge_taper_angle_deg)

    # Critical self-locking tangent threshold
    max_self_locking_tan = (inner_friction_coeff - outer_ptfe_friction) / (
        1.0 + inner_friction_coeff * outer_ptfe_friction
    )
    is_self_locking = math.tan(alpha_rad) < max_self_locking_tan

    # Normal clamping force generated on each wedge jaw (kN)
    normal_clamping_force_kn = load_per_lock_kn / (
        2.0 * (inner_friction_coeff * math.cos(alpha_rad) + math.sin(alpha_rad))
    )

    return {
        "load_per_lock_kn": round(load_per_lock_kn, 2),
        "normal_force_kn": round(normal_clamping_force_kn, 2),
        "self_locking_0w": is_self_locking,
    }


def evaluate_light_frame_safety_factor(
    frame_mass_kg=74.0,
    payload_mass_kg=40.0,
    dynamic_g_factor=2.5,
    material="7075-T6_Aluminum",
    cross_section_area_mm2=420.0,
):
    """
    Evaluates structural stress and safety factor for the 74 kg Inner Frame skeleton
    under peak dynamic walking/lifting loads (2.5 G) using lightweight aerospace materials.
    """
    material_yield_mpa = {
        "7075-T6_Aluminum": 503.0,
        "Carbon_Fiber_T700": 1500.0,
    }

    yield_strength = material_yield_mpa.get(material, 503.0)
    total_dynamic_force_n = (frame_mass_kg + payload_mass_kg) * 9.81 * dynamic_g_factor

    # Stress in MPa (1 N / 1 mm^2 = 1 MPa)
    applied_stress_mpa = total_dynamic_force_n / cross_section_area_mm2
    safety_factor = yield_strength / applied_stress_mpa if applied_stress_mpa > 0 else 0.0

    return {
        "material": material,
        "peak_load_kn": round(total_dynamic_force_n / 1000.0, 2),
        "applied_stress_mpa": round(applied_stress_mpa, 1),
        "safety_factor": round(safety_factor, 2),
    }


if __name__ == "__main__":
    print("--- BioFrame Light (74 kg): 4-Stage Joint & Structural Scaling ---")

    # 1. 4-stage segmented knee/elbow bend (140 deg total -> 35 deg per stage)
    seg_angle, eff = calculate_segmented_joint_capstan_efficiency(140.0, num_segments=4)
    print(f"1. 4-Stage Joint Articulation: {seg_angle} deg/segment | Tendon Efficiency: {eff}%")

    # 2. Dual-opposing 0-Watt magnetic wedge lock holding capacity (74 kg + 40 kg load)
    lock_metrics = calculate_wedge_lock_holding_capacity(total_limb_load_kn=2.8, parallel_locks=2)
    print(
        f"2. 0W Magnetic Wedge Lock: {lock_metrics['load_per_lock_kn']} kN/lock | "
        f"Clamping Force: {lock_metrics['normal_force_kn']} kN | Self-Locking: {lock_metrics['self_locking_0w']}"
    )

    # 3. Structural safety factor for 7075-T6 Aluminum vs. T700 Carbon Fiber Inner Frame
    alu_metrics = evaluate_light_frame_safety_factor(material="7075-T6_Aluminum")
    cf_metrics = evaluate_light_frame_safety_factor(material="Carbon_Fiber_T700")
    print(
        f"3. Frame Safety Factor (2.5G Peak): {alu_metrics['safety_factor']}x (7075-T6 Alu) | "
        f"{cf_metrics['safety_factor']}x (T700 Carbon)"
    )

