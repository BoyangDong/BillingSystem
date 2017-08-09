<!-- Button Start New -->
<!-- Modal -->
<div class="modal fade" id="start-new-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" style="width=20px;">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
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
								<input class="form-check-input" type="checkbox" id="corey" name="recurring_group[]" value="rent"> Rent
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="mark" name="recurring_group[]" value="tech_fee"> Tech Fee
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="gary" name="recurring_group[]" value="server_use"> Server Use
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="becky" name="recurring_group[]" value="pc_use"> PC Use
							</label>
						</div>
					</div>
					<div class="col-lg-5">	
						<label class="control-label" for="title">Load Vendor Charge</label>			
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang" name="recurring_group[]" value="victory"> Victory
							</label>
						</div>	
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang2" name="recurring_group[]" value="optionscity"> OptionsCity
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang2" name="recurring_group[]" value="rival"> Rival
							</label>
						</div>		
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang2" name="recurring_group[]" value="actant"> Actant
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang2" name="recurring_group[]" value="blue_cross"> Blue Cross Blue Shield
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang2" name="recurring_group[]" value="euclid"> Euclid (Dental Insurance)
							</label>
						</div>		
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang2" name="recurring_group[]" value="cloud9"> Cloud9
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
						<label class="control-label" for="title">All the existing billings will be gone, are you sure?</label>
					<div class="col-lg-1">
					</div>
				</div>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-default" data-dismiss="modal">Ignore</button>
				<button type="button" id="confirm_delete" class="btn btn-danger" data-dismiss="modal">Proceed</button>
			</div>
		</div>
	</div>
</div>


