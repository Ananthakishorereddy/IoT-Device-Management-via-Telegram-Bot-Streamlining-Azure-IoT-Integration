from provisioningserviceclient import ProvisioningServiceClient
from provisioningserviceclient.models import IndividualEnrollment, AttestationMechanism

provisioning_host = "HostName"
id_scope = "IdScope"
connection_string = "ConnectionString"
registration_id = "RegistrationId"

client = ProvisioningServiceClient.create_from_connection_string(connection_string)

attestation = AttestationMechanism.create_with_tpm(registration_id)

individual_enrollment = IndividualEnrollment.create(registration_id, attestation)
individual_enrollment.device_id = "myDeviceId"
individual_enrollment.provisioning_status = "enabled"

client.create_or_update(id_scope, IndividualEnrollment, individual_enrollment)