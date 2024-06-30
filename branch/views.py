from django.shortcuts import render
from analysis.models import Data
import os

def civil_engineering_4_years_bachelor_of_technology(request):
    branch_name = "civil_engineering_4_years_bachelor_of_technology"
    filtered_data_points = Data.objects.filter(Branch__contains=branch_name)
    print(filtered_data_points)

    Institue = [point.Institue for point in filtered_data_points]
    Branch = [point.Branch for point in filtered_data_points]
    Quota = [point.Quota for point in filtered_data_points]
    Seat_Type = [point.Seat_Type for point in filtered_data_points]
    Opening_Rank = [point.Opening_Rank for point in filtered_data_points]
    Closing_Rank = [point.Closing_Rank for point in filtered_data_points]
    Year = [point.Year for point in filtered_data_points]
    Round = [point.Round for point in filtered_data_points]
    
    context = {
        'Institue': Institue,
        'Branch': Branch,
        'Quota': Quota,
        'Seat_Type': Seat_Type,
        'Opening_Rank': Opening_Rank,
        'Closing_Rank': Closing_Rank,
        'Year': Year,
        'Round': Round,
    }
     
    return render(request, 'branch/civil_engineering_4_years_bachelor_of_technology.html', context)

def computer_science_and_engineering_4_years_bachelor_of_technology(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_4_years_bachelor_of_technology.html')


def electrical_engineering_4_years_bachelor_of_technology(request):
     #data = DAta.objects.all()
     return render(request,'branch/electrical_engineering_4_years_bachelor_of_technology.html')


def electronics_and_communication_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_communication_engineering_4_years_bachelor_of_technology_.html')


def engineering_physics_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/engineering_physics_4_years_bachelor_of_technology_.html')


def mechanical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mechanical_engineering_4_years_bachelor_of_technology_.html')


def metallurgical_and_materials_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/metallurgical_and_materials_engineering_4_years_bachelor_of_technology_.html')


def aerospace_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/aerospace_engineering_4_years_bachelor_of_technology_.html')


def chemical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemical_engineering_4_years_bachelor_of_technology_.html')


def environmental_science_and_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/environmental_science_and_engineering_4_years_bachelor_of_technology_.html')


def metallurgical_engineering_and_materials_science_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/metallurgical_engineering_and_materials_science_4_years_bachelor_of_technology_.html')


def industrial_engineering_and_operations_research_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/industrial_engineering_and_operations_research_4_years_bachelor_of_technology_.html')


def energy_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/energy_engineering_4_years_bachelor_of_technology_.html')


def chemistry_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemistry_4_years_bachelor_of_science_.html')


def economics_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/economics_4_years_bachelor_of_science_.html')


def bs_in_mathematics_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/bs_in_mathematics_4_years_bachelor_of_science_.html')


def electrical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electrical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def btech_in_general_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_general_engineering_4_years_bachelor_of_technology_.html')


def btech_in_materials_science_and_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_materials_science_and_engineering_4_years_bachelor_of_technology_.html')


def btech_in_microelectronics_amp_vlsi_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_microelectronics_amp_vlsi_4_years_bachelor_of_technology_.html')


def btech_in_mathematics_and_computing_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_mathematics_and_computing_4_years_bachelor_of_technology_.html')


def bio_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/bio_engineering_4_years_bachelor_of_technology_.html')


def data_science_and_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/data_science_and_engineering_4_years_bachelor_of_technology_.html')


def bs_in_chemical_sciences_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/bs_in_chemical_sciences_4_years_bachelor_of_science_.html')


def biotechnology_and_biochemical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/biotechnology_and_biochemical_engineering_4_years_bachelor_of_technology_.html')


def electrical_engineering_power_and_automation_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electrical_engineering_power_and_automation_4_years_bachelor_of_technology_.html')


def mathematics_and_computing_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_and_computing_4_years_bachelor_of_technology_.html')


def production_and_industrial_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/production_and_industrial_engineering_4_years_bachelor_of_technology_.html')


def textile_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/textile_technology_4_years_bachelor_of_technology_.html')


def engineering_and_computational_mechanics_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/engineering_and_computational_mechanics_4_years_bachelor_of_technology_.html')


def materials_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/materials_engineering_4_years_bachelor_of_technology_.html')


def chemical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def computer_science_and_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def mathematics_and_computing_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_and_computing_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def space_sciences_and_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/space_sciences_and_engineering_4_years_bachelor_of_technology_.html')


def agricultural_and_food_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/agricultural_and_food_engineering_4_years_bachelor_of_technology_.html')


def electronics_and_electrical_communication_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_electrical_communication_engineering_4_years_bachelor_of_technology_.html')


def instrumentation_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/instrumentation_engineering_4_years_bachelor_of_technology_.html')


def manufacturing_science_and_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/manufacturing_science_and_engineering_4_years_bachelor_of_technology_.html')


def mining_engineering__4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mining_engineering__4_years_bachelor_of_technology_.html')


def ocean_engineering_and_naval_architecture_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/ocean_engineering_and_naval_architecture_4_years_bachelor_of_technology_.html')


def industrial_and_systems_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/industrial_and_systems_engineering_4_years_bachelor_of_technology_.html')


def artificial_intelligence_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/artificial_intelligence_4_years_bachelor_of_technology_.html')


def physics_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/physics_4_years_bachelor_of_science_.html')


def mathematics_and_computing_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_and_computing_4_years_bachelor_of_science_.html')


def applied_geology_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/applied_geology_4_years_bachelor_of_science_.html')


def exploration_geophysics_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/exploration_geophysics_4_years_bachelor_of_science_.html')


def architecture__5_years_bachelor_of_architecture_(request):
     #data = DAta.objects.all()
     return render(request,'branch/architecture__5_years_bachelor_of_architecture_.html')


def computational_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computational_engineering_4_years_bachelor_of_technology_.html')


def industrial_chemistry_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/industrial_chemistry_4_years_bachelor_of_technology_.html')


def electrical_engineering_ic_design_and_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electrical_engineering_ic_design_and_technology_4_years_bachelor_of_technology_.html')


def engineering_science_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/engineering_science_4_years_bachelor_of_technology_.html')


def materials_science_and_metallurgical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/materials_science_and_metallurgical_engineering_4_years_bachelor_of_technology_.html')


def biomedical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/biomedical_engineering_4_years_bachelor_of_technology_.html')


def biotechnology_and_bioinformatics_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/biotechnology_and_bioinformatics_4_years_bachelor_of_technology_.html')


def civil_and_infrastructure_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/civil_and_infrastructure_engineering_4_years_bachelor_of_technology_.html')


def artificial_intelligence_and_data_science_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/artificial_intelligence_and_data_science_4_years_bachelor_of_technology_.html')


def physics_with_specialization_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/physics_with_specialization_4_years_bachelor_of_science_.html')


def chemistry_with_specialization_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemistry_with_specialization_4_years_bachelor_of_science_.html')


def biological_sciences_and_bioengineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/biological_sciences_and_bioengineering_4_years_bachelor_of_technology_.html')


def materials_science_and_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/materials_science_and_engineering_4_years_bachelor_of_technology_.html')


def mathematics_and_scientific_computing_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_and_scientific_computing_4_years_bachelor_of_science_.html')


def earth_sciences_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/earth_sciences_4_years_bachelor_of_science_.html')


def statistics_and_data_science_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/statistics_and_data_science_4_years_bachelor_of_science_.html')


def biological_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/biological_engineering_4_years_bachelor_of_technology_.html')


def naval_architecture_and_ocean_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/naval_architecture_and_ocean_engineering_4_years_bachelor_of_technology_.html')


def data_science_and_artificial_intelligence_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/data_science_and_artificial_intelligence_4_years_bachelor_of_technology_.html')


def biological_science_4_years_bachelor_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/biological_science_4_years_bachelor_of_science_.html')


def aerospace_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/aerospace_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def engineering_design_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/engineering_design_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def physics_5_years_bachelor_of_science_and_master_of_science_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/physics_5_years_bachelor_of_science_and_master_of_science_dual_degree_.html')


def integrated_circuit_design_amp_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/integrated_circuit_design_amp_technology_4_years_bachelor_of_technology_.html')


def mechanical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mechanical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def chemical_science_and_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemical_science_and_technology_4_years_bachelor_of_technology_.html')


def electrical_and_electronics_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electrical_and_electronics_engineering_4_years_bachelor_of_technology_.html')


def btech_in_electronics_and_communication_engineering_and_mtech_in_communication_systems_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_electronics_and_communication_engineering_and_mtech_in_communication_systems_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def btech_chemical_science_and_technology__mba_in_hospital_and_health_care_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_chemical_science_and_technology__mba_in_hospital_and_health_care_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_civil_engineering__mba_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_civil_engineering__mba_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_computer_science_and_engineering__mba_in_digital_business_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_computer_science_and_engineering__mba_in_digital_business_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_electronics_and_communication_engineering__mba_in_hospital_and_healthcare_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_electronics_and_communication_engineering__mba_in_hospital_and_healthcare_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_engineering_physics__mba_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_engineering_physics__mba_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_mathematics_and_computing__mba_in_digital_business_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_mathematics_and_computing__mba_in_digital_business_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_metallurgical_and_materials_engineering__mba_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_metallurgical_and_materials_engineering__mba_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_electrical_and_electronics_engineering__mba_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_electrical_and_electronics_engineering__mba_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_artificial_intelligence_and_data_science__mba_in_digital_business_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_artificial_intelligence_and_data_science__mba_in_digital_business_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_chemical_engineering__mba_in_hospital_and_health_care_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_chemical_engineering__mba_in_hospital_and_health_care_management_iim_bodh_gaya_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def btech_mechanical_engineering__mba_iim_mumbai_5_years_bachelor_of_technology_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_mechanical_engineering__mba_iim_mumbai_5_years_bachelor_of_technology_and_mba_dual_degree_.html')


def b_tech_in_ce__m_tech__in_geotechnical_engineering_5_years_btech__mtechms_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/b_tech_in_ce__m_tech__in_geotechnical_engineering_5_years_btech__mtechms_dual_degree_.html')


def b_tech_in_ce__m_tech__in_structural_engineering_5_years_btech__mtechms_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/b_tech_in_ce__m_tech__in_structural_engineering_5_years_btech__mtechms_dual_degree_.html')


def b_tech_cse_and_mtech_in_cse_5_years_btech__mtechms_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/b_tech_cse_and_mtech_in_cse_5_years_btech__mtechms_dual_degree_.html')


def b_tech_ece_m_tech_in_vlsi_5_years_btech__mtechms_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/b_tech_ece_m_tech_in_vlsi_5_years_btech__mtechms_dual_degree_.html')


def b_tech_eeem_tech_in_power_amp_control_5_years_btech__mtechms_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/b_tech_eeem_tech_in_power_amp_control_5_years_btech__mtechms_dual_degree_.html')


def b_tech_mathematics_amp_computing_m_tech_in_mathematics_amp_computing_5_years_btech__mtechms_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/b_tech_mathematics_amp_computing_m_tech_in_mathematics_amp_computing_5_years_btech__mtechms_dual_degree_.html')


def b_tech_me__m_tech_in_mechatronics_5_years_btech__mtechms_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/b_tech_me__m_tech_in_mechatronics_5_years_btech__mtechms_dual_degree_.html')


def bs_in_economics_with_mba_iim_bodh_gaya_5_years_bachelor_of_science_and_mba_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/bs_in_economics_with_mba_iim_bodh_gaya_5_years_bachelor_of_science_and_mba_dual_degree_.html')


def biosciences_and_bioengineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/biosciences_and_bioengineering_4_years_bachelor_of_technology_.html')


def geological_technology_5_years_integrated_master_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/geological_technology_5_years_integrated_master_of_technology_.html')


def geophysical_technology_5_years_integrated_master_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/geophysical_technology_5_years_integrated_master_of_technology_.html')


def mathematics_amp_computing_5_years_bachelor_of_science_and_master_of_science_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_amp_computing_5_years_bachelor_of_science_and_master_of_science_dual_degree_.html')


def chemical_sciences_5_years_bachelor_of_science_and_master_of_science_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemical_sciences_5_years_bachelor_of_science_and_master_of_science_dual_degree_.html')


def economics_5_years_bachelor_of_science_and_master_of_science_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/economics_5_years_bachelor_of_science_and_master_of_science_dual_degree_.html')


def environmental_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/environmental_engineering_4_years_bachelor_of_technology_.html')


def mining_machinery_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mining_machinery_engineering_4_years_bachelor_of_technology_.html')


def petroleum_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/petroleum_engineering_4_years_bachelor_of_technology_.html')


def mineral_and_metallurgical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mineral_and_metallurgical_engineering_4_years_bachelor_of_technology_.html')


def applied_geology_5_years_integrated_master_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/applied_geology_5_years_integrated_master_of_technology_.html')


def applied_geophysics_5_years_integrated_master_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/applied_geophysics_5_years_integrated_master_of_technology_.html')


def artificial_intelligence_and_data_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/artificial_intelligence_and_data_engineering_4_years_bachelor_of_technology_.html')


def ceramic_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/ceramic_engineering_4_years_bachelor_of_technology_.html')


def electronics_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_engineering_4_years_bachelor_of_technology_.html')


def metallurgical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/metallurgical_engineering_4_years_bachelor_of_technology_.html')


def pharmaceutical_engineering_amp_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/pharmaceutical_engineering_amp_technology_4_years_bachelor_of_technology_.html')


def biochemical_engineering_with_mtech_in_biochemical_engineering_and_biotechnology_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/biochemical_engineering_with_mtech_in_biochemical_engineering_and_biotechnology_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def bioengineering_with_mtech_in_biomedical_technology_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/bioengineering_with_mtech_in_biomedical_technology_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def ceramic_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/ceramic_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def civil_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/civil_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def electrical_engineering_with_mtech_in_power_electronics_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electrical_engineering_with_mtech_in_power_electronics_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def materials_science_and_technology_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/materials_science_and_technology_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def metallurgical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/metallurgical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def mining_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mining_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def engineering_physics_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/engineering_physics_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def industrial_chemistry_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/industrial_chemistry_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def pharmaceutical_engineering_amp_technology_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/pharmaceutical_engineering_amp_technology_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def electronics_and_electrical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_electrical_engineering_4_years_bachelor_of_technology_.html')


def mechatronics_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mechatronics_engineering_4_years_bachelor_of_technology_.html')


def chemical_and_biochemical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemical_and_biochemical_engineering_4_years_bachelor_of_technology_.html')


def interdisciplinary_sciences_5_years_bachelor_of_science_and_master_of_science_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/interdisciplinary_sciences_5_years_bachelor_of_science_and_master_of_science_dual_degree_.html')


def bio_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/bio_technology_4_years_bachelor_of_technology_.html')


def electronics_and_vlsi_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_vlsi_engineering_4_years_bachelor_of_technology_.html')


def information_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/information_technology_4_years_bachelor_of_technology_.html')


def instrumentation_and_control_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/instrumentation_and_control_engineering_4_years_bachelor_of_technology_.html')


def industrial_and_production_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/industrial_and_production_engineering_4_years_bachelor_of_technology_.html')


def planning_4_years_bachelor_of_planning_(request):
     #data = DAta.objects.all()
     return render(request,'branch/planning_4_years_bachelor_of_planning_.html')


def mathematics_and_data_science_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_and_data_science_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def materials_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/materials_engineering_4_years_bachelor_of_technology_.html')


def electronics_and_instrumentation_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_instrumentation_engineering_4_years_bachelor_of_technology_.html')


def production_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/production_engineering_4_years_bachelor_of_technology_.html')


def computational_mathematics_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computational_mathematics_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def chemistry_5_years_bachelor_of_science_and_master_of_science_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemistry_5_years_bachelor_of_science_and_master_of_science_dual_degree_.html')


def vlsi_design_and_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/vlsi_design_and_technology_4_years_bachelor_of_technology_.html')


def chemical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemical_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def biotechnology_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/biotechnology_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def chemistry_5_years_integrated_master_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemistry_5_years_integrated_master_of_science_.html')


def electronics_and_communication_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_communication_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def computational_and_data_science_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computational_and_data_science_4_years_bachelor_of_technology_.html')


def mechatronics_and_automation_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mechatronics_and_automation_engineering_4_years_bachelor_of_technology_.html')


def computer_science_and_engineering_with_specialization_in_data_science_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_with_specialization_in_data_science_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def computer_science_and_engineering_with_specialization_in_cyber_security_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_with_specialization_in_cyber_security_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def electronics_and_communication_engineering_with_specialization_in_microelectronics_and_vlsi_system_design_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_communication_engineering_with_specialization_in_microelectronics_and_vlsi_system_design_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def electrical_engineering_with_specialization_in_power_system_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electrical_engineering_with_specialization_in_power_system_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def mechanical_engineering_with_specialization_in_manufacturing_and_industrial_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mechanical_engineering_with_specialization_in_manufacturing_and_industrial_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def civil_engineering_with_specialization_in_construction_technology_and_management_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/civil_engineering_with_specialization_in_construction_technology_and_management_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def material_science_and_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/material_science_and_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def mathematics_and_computing_technology_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_and_computing_technology_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def chemical_technology_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemical_technology_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def bio_medical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/bio_medical_engineering_4_years_bachelor_of_technology_.html')


def artificial_intelligence_and_machine_learning_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/artificial_intelligence_and_machine_learning_4_years_bachelor_of_technology_.html')


def industrial_internet_of_things_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/industrial_internet_of_things_4_years_bachelor_of_technology_.html')


def robotics_amp_automation_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/robotics_amp_automation_4_years_bachelor_of_technology_.html')


def microelectronics_amp_vlsi_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/microelectronics_amp_vlsi_engineering_4_years_bachelor_of_technology_.html')


def sustainable_energy_technologies_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/sustainable_energy_technologies_4_years_bachelor_of_technology_.html')


def architecture_and_planning_5_years_bachelor_of_architecture_(request):
     #data = DAta.objects.all()
     return render(request,'branch/architecture_and_planning_5_years_bachelor_of_architecture_.html')


def industrial_design_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/industrial_design_4_years_bachelor_of_technology_.html')


def food_process_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/food_process_engineering_4_years_bachelor_of_technology_.html')


def metallurgical_and_materials_engineering_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/metallurgical_and_materials_engineering_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def ceramic_engineering_and_mtech_industrial_ceramic_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/ceramic_engineering_and_mtech_industrial_ceramic_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def physics_5_years_integrated_master_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/physics_5_years_integrated_master_of_science_.html')


def mathematics_5_years_integrated_master_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_5_years_integrated_master_of_science_.html')


def life_science_5_years_integrated_master_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/life_science_5_years_integrated_master_of_science_.html')


def electronics_and_communication_engineering_vlsi_design_and_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_communication_engineering_vlsi_design_and_technology_4_years_bachelor_of_technology_.html')


def computer_science_and_engineering__artificial_intelligence_amp_data_science_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering__artificial_intelligence_amp_data_science_4_years_bachelor_of_technology_.html')


def artificial_intelligence_5_years_integrated_b_tech_and_m_tech_(request):
     #data = DAta.objects.all()
     return render(request,'branch/artificial_intelligence_5_years_integrated_b_tech_and_m_tech_.html')


def electronics_and_telecommunication_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_telecommunication_engineering_4_years_bachelor_of_technology_.html')


def metallurgy_and_materials_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/metallurgy_and_materials_engineering_4_years_bachelor_of_technology_.html')


def mathematics_and_scientific_computing_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_and_scientific_computing_4_years_bachelor_of_technology_.html')


def integrated_b_techit_and_m_tech_it_5_years_integrated_b_tech_and_m_tech_(request):
     #data = DAta.objects.all()
     return render(request,'branch/integrated_b_techit_and_m_tech_it_5_years_integrated_b_tech_and_m_tech_.html')


def integrated_b_techit_and_mba_5_years_integrated_b_tech_and_mba_(request):
     #data = DAta.objects.all()
     return render(request,'branch/integrated_b_techit_and_mba_5_years_integrated_b_tech_and_mba_.html')


def cse__data_science_amp_analytics_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/cse__data_science_amp_analytics_4_years_bachelor_of_technology_.html')


def computer_science_and_engineering_cyber_security_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_cyber_security_4_years_bachelor_of_technology_.html')


def computer_science_and_engineering_data_science_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_data_science_4_years_bachelor_of_technology_.html')


def information_technologybusiness_informatics_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/information_technologybusiness_informatics_4_years_bachelor_of_technology_.html')


def smart_manufacturing_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/smart_manufacturing_4_years_bachelor_of_technology_.html')


def computer_science_and_engineering_with_major_in_artificial_intelligence_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_with_major_in_artificial_intelligence_4_years_bachelor_of_technology_.html')


def btech_in_electronics_and_communication_engineering_and_mtech_in_vlsi_design_5_years_bachelor_and_master_of_technology_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_electronics_and_communication_engineering_and_mtech_in_vlsi_design_5_years_bachelor_and_master_of_technology_dual_degree_.html')


def btech_in_mechanical_engineering_and_mtech_in_ai_and_robotics_5_years_btech__mtechms_dual_degree_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_mechanical_engineering_and_mtech_in_ai_and_robotics_5_years_btech__mtechms_dual_degree_.html')


def electronics_and_communication_engineering_with_specialization_in_vlsi_and_embedded_systems_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_communication_engineering_with_specialization_in_vlsi_and_embedded_systems_4_years_bachelor_of_technology_.html')


def computer_science_and_engineering_with_specialization_in_artificial_intelligence_and_data_science_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_with_specialization_in_artificial_intelligence_and_data_science_4_years_bachelor_of_technology_.html')


def computer_science_and_business_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_business_4_years_bachelor_of_technology_.html')


def computer_science_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_4_years_bachelor_of_technology_.html')


def computer_science_and_artificial_intelligence_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_artificial_intelligence_4_years_bachelor_of_technology_.html')


def electronics_and_communication_engineering_with_specialization_in_design_and_manufacturing_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_communication_engineering_with_specialization_in_design_and_manufacturing_4_years_bachelor_of_technology_.html')


def mechanical_engineering_with_specialization_in_design_and_manufacturing_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mechanical_engineering_with_specialization_in_design_and_manufacturing_4_years_bachelor_of_technology_.html')


def computer_science_and_engineering_with_specialization_in_cyber_security_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_with_specialization_in_cyber_security_4_years_bachelor_of_technology_.html')


def electronics_and_communication_engineering_with_specialization_of_embedded_systems_and_internet_of_things_4_years_b_tech__b_tech_hons_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_communication_engineering_with_specialization_of_embedded_systems_and_internet_of_things_4_years_b_tech__b_tech_hons_.html')


def computer_science_and_engineering_with_specialization_of_data_science_and_artificial_intelligence4_years_b_tech__b_tech_hons_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_with_specialization_of_data_science_and_artificial_intelligence4_years_b_tech__b_tech_hons_.html')


def computer_science_engineering_artificial_lntelligence_and_machine_learning_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_engineering_artificial_lntelligence_and_machine_learning_4_years_bachelor_of_technology_.html')


def computer_science_engineering_data_science_and_analytics_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_engineering_data_science_and_analytics_4_years_bachelor_of_technology_.html')


def computer_science_engineering_human_computer_lnteraction_and_gaming_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_engineering_human_computer_lnteraction_and_gaming_technology_4_years_bachelor_of_technology_.html')


def electronics_and_communication_engineering_internet_of_things_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_communication_engineering_internet_of_things_4_years_bachelor_of_technology_.html')


def computer_science_and_engineering_cyber_physical_system_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_cyber_physical_system_4_years_bachelor_of_technology_.html')


def computer_science_and_engineering_artificial_intelligence_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_and_engineering_artificial_intelligence_4_years_bachelor_of_technology_.html')


def agricultural_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/agricultural_engineering_4_years_bachelor_of_technology_.html')


def food_engineering__and_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/food_engineering__and_technology_4_years_bachelor_of_technology_.html')


def mathematics_and_computing_5_years_integrated_master_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/mathematics_and_computing_5_years_integrated_master_of_science_.html')


def quantitative_economics_amp_data_science_5_years_integrated_master_of_science_(request):
     #data = DAta.objects.all()
     return render(request,'branch/quantitative_economics_amp_data_science_5_years_integrated_master_of_science_.html')


def carpet__and_textile_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/carpet__and_textile_technology_4_years_bachelor_of_technology_.html')


def computer_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_engineering_4_years_bachelor_of_technology_.html')


def electronic_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronic_engineering_4_years_bachelor_of_technology_.html')


def food_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/food_technology_4_years_bachelor_of_technology_.html')


def bachelor_of_design_4_years_bachelor_of_design_(request):
     #data = DAta.objects.all()
     return render(request,'branch/bachelor_of_design_4_years_bachelor_of_design_.html')


def materials_engineering_5_years_integrated_master_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/materials_engineering_5_years_integrated_master_of_technology_.html')


def electronics_engineering_vlsi_design_and_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_engineering_vlsi_design_and_technology_4_years_bachelor_of_technology_.html')


def computer_science_engineering_artificial_intelligence_4_years_b_tech__b_tech_hons_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_engineering_artificial_intelligence_4_years_b_tech__b_tech_hons_.html')


def computer_science_engineering_data_science_4_years_b_tech__b_tech_hons_(request):
     #data = DAta.objects.all()
     return render(request,'branch/computer_science_engineering_data_science_4_years_b_tech__b_tech_hons_.html')


def civil_and_environmental_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/civil_and_environmental_engineering_4_years_bachelor_of_technology_.html')


def food_technology_and_management_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/food_technology_and_management_4_years_bachelor_of_technology_.html')


def handloom_and_textile_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/handloom_and_textile_technology_4_years_bachelor_of_technology_.html')


def chemical_engineering_5_years_integrated_masters_in_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/chemical_engineering_5_years_integrated_masters_in_technology_.html')


def electronics_and_communication_engineering_avionics_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/electronics_and_communication_engineering_avionics_4_years_bachelor_of_technology_.html')


def aeronautical_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/aeronautical_engineering_4_years_bachelor_of_technology_.html')


def dairy_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/dairy_engineering_4_years_bachelor_of_technology_.html')


def fashion_and_apparel_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/fashion_and_apparel_engineering_4_years_bachelor_of_technology_.html')


def printing_and_packaging_technology_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/printing_and_packaging_technology_4_years_bachelor_of_technology_.html')


def btech_in_electronics_amp_communication_engineering_rail_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_electronics_amp_communication_engineering_rail_engineering_4_years_bachelor_of_technology_.html')


def btech_in_electrical_engineering__rail__engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_electrical_engineering__rail__engineering_4_years_bachelor_of_technology_.html')


def btech_in_mechanical_engineering__rail__engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_mechanical_engineering__rail__engineering_4_years_bachelor_of_technology_.html')


def btech_in_civil_engineering_rail_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_civil_engineering_rail_engineering_4_years_bachelor_of_technology_.html')


def btech_in_artificial_intelligenece_and_data_science_transportation_and_logistics_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_artificial_intelligenece_and_data_science_transportation_and_logistics_4_years_bachelor_of_technology_.html')


def btech_in_aviation_engineering_4_years_bachelor_of_technology_(request):
     #data = DAta.objects.all()
     return render(request,'branch/btech_in_aviation_engineering_4_years_bachelor_of_technology_.html')


def integrated_b_tech_m_tech_in_metallurgical_amp_materials_engineering_5_years_integrated_b_tech_and_m_tech_(request):
     #data = DAta.objects.all()
     return render(request,'branch/integrated_b_tech_m_tech_in_metallurgical_amp_materials_engineering_5_years_integrated_b_tech_and_m_tech_.html')


def integrated_b_tech__m_tech_in_electrical_engineering_5_years_integrated_b_tech_and_m_tech_(request):
     #data = DAta.objects.all()
     return render(request,'branch/integrated_b_tech__m_tech_in_electrical_engineering_5_years_integrated_b_tech_and_m_tech_.html')


def integrated_b_tech__m_tech_in_civil_engineering_5_years_integrated_b_tech_and_m_tech_(request):
     #data = DAta.objects.all()
     return render(request,'branch/integrated_b_tech__m_tech_in_civil_engineering_5_years_integrated_b_tech_and_m_tech_.html')


def integrated_b_tech__m_tech_in_computer_science_amp_engineering_5_years_integrated_b_tech_and_m_tech_(request):
     #data = DAta.objects.all()
     return render(request,'branch/integrated_b_tech__m_tech_in_computer_science_amp_engineering_5_years_integrated_b_tech_and_m_tech_.html')







#def Aeronautical_Engineering_4_Years_Bachelor_of_Technology(request):
    #data = Data.objects.all()
    # return render(request,'branch/Aeronautical_Engineering_4_Years_Bachelor_of_Technology.html')
    
    


    




#directory_name = 'branch/'

#for file in os.listdir(directory_name):
 #       if file.endswith('.html'):
  #          def file(request):
   #              file_path = os.path.join(directory_name, file)
    #             return render(request,file_path)


# Create your views here.
