<!--SUBMIT SHEET MODAL-->
<div class="modal fade" id="submit-modal" tabindex="-1" role="dialog" aria-labelledby="createLabel"> 
	<div class="modal-dialog" role="document"> 
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
		        <h4 class="modal-title" id="editLabel"><strong>Submit for Approval</strong></h4>
			</div>
			<div class="modal-body"> 
				<div class="form-group">
					<form action="api/send_email.php" method="POST">
						<p>Select Recipients</p>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="corey" name="recipients" value="corey.fisher@budoholdings.com" disabled> Corey F.
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="mark" name="recipients" value="mark.cukier@budoholdings.com" disabled> Mark C.
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="gary" name="recipients" value="gary.patzik@budoholdings.com" disabled> Gary P.
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="becky" name="recipients" value="becky.ali@budoholdings.com" disabled> Becky A.
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang" name="recipients" value="boyang.dong@budoholdings.com"> Boyang D.
							</label>
						</div>	
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang2" name="recipients" value="bdong.bobo@gmail.com"> Boyang Gmail
							</label>
						</div>					
						<p style="margin-top: 5px; margin-bottom: 2px;">Title</p>
						<input type="text" name="mail_sub" class="form-control" value="Today's Rebill Sheet"/>
						<p style="margin-top: 10px; margin-bottom: 2px;">Content</p>
						<textarea rows='4' name="mail_msg" class="form-control" data-error="Please say something..." required>Hi all, please checkout the file attached..&#13;&#10;&#13;&#10;Thanks,&#13;&#10;Becky</textarea>
						<p style="margin-top: 10px; margin-bottom: 2px;">Attachement</p>
						<div class="form-group">
							<button class="btn btn-success send-email">GO!</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>

</div>