<!-- Button Start New -->
<!-- Modal -->
<div class="modal fade" id="start-new-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" style="width=20px;">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<form action="api/delete_all.php" name="loadRecurringCharge" method="POST">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
					<h4 class="modal-title" id="myModalLabel"><b>Start a New Sheet</b></h4>
				</div>
				<div class="modal-body">
					<div class="row"> 
						<div class="col-lg-1"></div>
						<div class="col-lg-5">
							<div class="form-group">
								<label class="control-label" for="title">Pick a Date</label>
									<input type="date" id="date_selector" name="date" required />
							</div>
						</div>
						<div class="col-lg-5"></div>
						<div class="col-lg-1"></div>					
					</div>
					<br/>
					<div class="row">
						<div class="col-lg-1">
						</div>
						<div class="col-lg-5"> 
							<label class="control-label" for="title">Load Budo Charge</label>
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="rent" name="recurring_group[]" value="Rent"> Rent
								</label>
							</div>
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="tech_fee" name="recurring_group[]" value="Tech_Fee"> Tech Fee
								</label>
							</div>
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="server_use" name="recurring_group[]" value="Server_Use"> Server Use
								</label>
							</div>
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="pc_use" name="recurring_group[]" value="PC_Use"> PC Use
								</label>
							</div>
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="others" name="recurring_group[]" value="Others"> Others
								</label>
							</div>
						</div>
						<div class="col-lg-5">	
							<label class="control-label" for="title">Load Vendor Charge</label>			
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="victory" name="recurring_group[]" value="victory" disabled="disabled"> Victory
								</label>
							</div>	
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="optionscity" name="recurring_group[]" value="optionscity" disabled="disabled"> OptionsCity
								</label>
							</div>
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="rivalsystems" name="recurring_group[]" value="rival" disabled="disabled"> RivalSystems
								</label>
							</div>		
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="actant" name="recurring_group[]" value="actant" disabled="disabled"> Actant
								</label>
							</div>
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="blue_cross" name="recurring_group[]" value="blue_cross" disabled="disabled"> Blue Cross Blue Shield
								</label>
							</div>
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="euclid" name="recurring_group[]" value="euclid" disabled="disabled"> Euclid (Dental Insurance)
								</label>
							</div>		
							<div class="form-check form-check-inline">
								<label class="form-check-label">
									<input class="form-check-input" type="checkbox" id="cloud9" name="recurring_group[]" value="cloud9" disabled="disabled"> Cloud9
								</label>
							</div>
							<br>
						</div>
						<div class="col-lg-1">
						</div>
					</div>
					<div class="row"> 
						<div class="col-lg-1">
						</div>
						<div class="col-lg-10"></div>
							<label class="control-label" for="title">Are you sure to start a new one? Current bills will be flushed out!</label>
						<div class="col-lg-1">
						</div>
					</div>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">Ignore</button>
					<button type="button" id="confirm_delete" class="btn btn-danger" data-dismiss="modal">Proceed</button>
				</div>
			</form>
		</div>
	</div>
</div>


